// Generates a commission-only Agent Agreement (.docx) on RS Links letterhead,
// for independent agents who refer candidates (not employees).
// Usage: node scripts/make-agent-agreement.js contracts/<agent>.json [out.docx]

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Header, Footer, ImageRun, Table,
  TableRow, TableCell, WidthType, BorderStyle, AlignmentType, PageNumber,
  LevelFormat, ShadingType, HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom,
} = require("docx");

const COMPANY = "RS Links Consultants (Pvt.) Ltd.";
const BRAND = "0E6143";
const COMPANY_ADDRESS = "Office No. 20, 3rd Floor, Satellite Shopping Centre, Sixth Road, Rawalpindi, Pakistan";
const FONT = "Calibri";
const LETTERHEAD_DIR = path.join(__dirname, "..", "templates", "letterhead");

const inFile = process.argv[2];
if (!inFile) {
  console.error("Usage: node scripts/make-agent-agreement.js <agent.json> [out.docx]");
  process.exit(1);
}
const a = JSON.parse(fs.readFileSync(inFile, "utf8"));
const outFile = process.argv[3] || inFile.replace(/\.json$/, ".docx");
const pkr = (n) => `PKR ${n.toLocaleString("en-US")}/-`;

const r = (text, opts = {}) => new TextRun({ text, font: FONT, size: 22, ...opts });
const b = (text, opts = {}) => r(text, { bold: true, ...opts });
const kids = (c) => (Array.isArray(c) ? c : [c]).map((x) => (typeof x === "string" ? r(x) : x));
const p = (children, opts = {}) => new Paragraph({ children: kids(children),
  spacing: { after: 120, line: 276 }, alignment: AlignmentType.JUSTIFIED, ...opts });

let clauseNo = 0;
const clause = (title) => {
  clauseNo += 1;
  return new Paragraph({ children: [b(`${clauseNo}. ${title.toUpperCase()}`, { color: BRAND })],
    spacing: { before: 200, after: 100 }, keepNext: true });
};
const sub = (children, opts = {}) => new Paragraph({ children: kids(children),
  numbering: { reference: "sub", level: 0, instance: clauseNo },
  spacing: { after: 80, line: 276 }, alignment: AlignmentType.JUSTIFIED, ...opts });

const background = (file) => new Header({ children: [new Paragraph({ children: [
  new ImageRun({ type: "jpg", data: fs.readFileSync(path.join(LETTERHEAD_DIR, file)),
    transformation: { width: 795, height: 1124 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 },
      behindDocument: true, allowOverlap: true,
    } }),
] })] });

const footer = new Footer({ children: [new Paragraph({ alignment: AlignmentType.RIGHT, children: [
  r(`Agent Agreement — ${a.name}  |  Page `, { size: 16, color: "6B7C75" }),
  new TextRun({ children: [PageNumber.CURRENT], size: 16, color: "6B7C75", font: FONT }),
  r(" of ", { size: 16, color: "6B7C75" }),
  new TextRun({ children: [PageNumber.TOTAL_PAGES], size: 16, color: "6B7C75", font: FONT }),
] })] });

const MARGIN_X = 1000;
const W = 11906 - 2 * MARGIN_X;
const line = { style: BorderStyle.SINGLE, size: 4, color: "B8D4C7" };
const borders = { top: line, bottom: line, left: line, right: line };
const cell = (child, w, shade, keep) => new TableCell({ width: { size: w, type: WidthType.DXA }, borders,
  ...(shade ? { shading: { type: ShadingType.CLEAR, fill: "E8F3EE", color: "auto" } } : {}),
  margins: { top: 60, bottom: 60, left: 120, right: 120 },
  children: [new Paragraph({ keepNext: !!keep, children: [child] })] });

const KC = [2800, W - 2800];
const terms = new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: KC, rows: [
  ["Agent Name", a.name], ["Father's Name", a.fatherName], ["CNIC No.", a.cnic],
  ...(a.address ? [["Address", a.address]] : []),
  ["Engagement", "Independent Agent (non-employee), commission only"],
  ["Scope", "Sourcing and referring candidates to the Company"],
  ["Charges to Candidates", "None — the Agent shall not charge candidates anything"],
  ["Effective Date", a.effectiveDate],
].map(([k, v]) => new TableRow({ children: [cell(b(k), KC[0], true), cell(r(v), KC[1])] })) });

const CC = [W - 720 - 3200, 3200];
const commissionTable = new Table({ width: { size: W - 720, type: WidthType.DXA }, columnWidths: CC,
  indent: { size: 720, type: WidthType.DXA }, rows: [
    new TableRow({ children: [cell(b("Destination"), CC[0], true, true), cell(b("Commission per Successful Case"), CC[1], true, true)] }),
    ...a.commission.map(([d, amt]) => new TableRow({ cantSplit: true, children: [
      cell(r(d), CC[0], false, true), cell(b(pkr(amt)), CC[1], false, true)] })),
  ] });

const sigBlock = (left, right) => {
  const half = W / 2;
  const none = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
  const nb = { top: none, bottom: none, left: none, right: none };
  const col = (lines) => new TableCell({ width: { size: half, type: WidthType.DXA }, borders: nb,
    children: lines.map((l, i) => new Paragraph({ spacing: { after: 60 },
      children: [i === 0 ? b(l, { color: BRAND }) : r(l)] })) });
  return new Table({ width: { size: W, type: WidthType.DXA }, columnWidths: [half, half],
    rows: [new TableRow({ cantSplit: true, children: [col(left), col(right)] })] });
};

const body = [
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 60 },
    children: [b("AGENT AGREEMENT", { size: 32, color: BRAND })] }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
    children: [r("Candidate Referral — Commission Only", { size: 24, italics: true })] }),

  p(["This Agent Agreement (the ", b("“Agreement”"), ") is made and entered into on the date stated above by and between:"]),
  p([b(COMPANY), `, a private limited company incorporated under the laws of Pakistan, having its office at ${COMPANY_ADDRESS} (hereinafter the `, b("“Company”"), ", which expression shall include its successors and assigns);"]),
  p([b("AND", { color: BRAND })], { alignment: AlignmentType.CENTER }),
  p([b(`${a.salutation} ${a.name}`), `, ${a.relation} ${a.fatherName}, holding CNIC No. `, b(a.cnic),
    `${a.address ? `, resident of ${a.address}` : ""} (hereinafter the `, b("“Agent”"), ")."]),
  p("The Company and the Agent are each referred to as a “Party” and together as the “Parties”. The Parties agree to the following terms and conditions."),

  new Paragraph({ spacing: { before: 120, after: 100 }, children: [b("KEY TERMS", { color: BRAND })] }),
  terms,

  clause("Appointment"),
  sub("The Company appoints the Agent, on a non-exclusive basis, to source and refer suitable candidates for the Company's overseas job orders, and the Agent accepts this appointment on the terms of this Agreement."),
  sub("The Company is free to appoint other agents and to source candidates through any other channel."),

  clause("Nature of Relationship — Not an Employee"),
  sub("The Agent is an independent agent and is not an employee, partner or legal representative of the Company. Nothing in this Agreement creates an employment relationship between the Parties."),
  sub("The Agent shall not be entitled to any salary, allowance, leave, bonus, gratuity, or any other employee benefit. The commission under this Agreement is the Agent's only compensation."),
  sub("The Agent shall bear their own expenses (including travel, phone and communication costs) and shall be responsible for their own taxes, unless otherwise agreed in writing."),
  sub("The Agent has no authority to sign any document, make any commitment, or accept any payment on behalf of the Company, and shall not present themself as an employee or officer of the Company."),

  clause("Scope of Work"),
  sub("The Agent shall source and refer genuine candidates who meet the requirements of the Company's job orders, as communicated by the Company from time to time."),
  sub("The Agent shall share accurate candidate details and documents with the Company, and shall assist candidates in completing the documentation the Company requires."),
  sub("Every candidate shall be registered with the Company, and all processing, counselling on costs, and payments shall be handled by the Company."),

  clause("No Charges to Candidates"),
  sub(["The Agent shall ", b("not charge, demand or receive any fee, money, gift or other benefit"), " from any candidate, their family or any other person, in any form or under any name, for referring or processing a candidate."]),
  sub("All payments by candidates shall be made only to the Company — to its official bank account or against an official Company receipt. The Agent shall not collect any payment on the Company's behalf or in their own name."),
  sub("The Agent shall quote to candidates only the official rates and terms communicated by the Company, and shall not add any amount to them."),
  sub("Any breach of this clause shall be a material breach entitling the Company to terminate this Agreement immediately, forfeit any unpaid commission on the affected cases, recover any loss, and report the matter to the relevant authorities."),

  clause("Commission"),
  sub("The Company shall pay the Agent a commission, out of the fee the Company receives for the case, for every Successful Case at the following rates:", { keepNext: true }),
  commissionTable,
  new Paragraph({ spacing: { after: 80 }, children: [] }),
  sub(["A ", b("“Successful Case”"), " means a candidate who (i) was referred by the Agent and registered with the Company under the Agent's name, (ii) whose case is approved, and (iii) for whom the Company has received full payment."]),
  sub(`Commission shall become payable only after the Company has received full payment for the case, and shall be paid ${a.payoutTiming}, by bank transfer or other agreed mode. Any tax required by law shall be deducted.`),
  sub("No commission shall be payable on a case for which full payment is not received, or which is cancelled or refunded. Where commission has already been paid on a case that is later refunded, the Agent shall return it, or the Company may adjust it against future commission."),
  sub("The Company's records of referrals, approvals and payments shall be the basis for calculating commission. Where two parties claim the same candidate, the candidate shall be credited to whoever registered the candidate with the Company first."),

  clause("Conduct and Compliance"),
  sub("The Agent shall act honestly and professionally, and shall not make any false or misleading promise or statement to a candidate about jobs, visas, salaries, timelines or costs."),
  sub("The Agent shall not prepare, alter or submit any forged, false or misleading document, and shall refer only candidates whose information they believe to be true."),
  sub("The Agent shall comply with all applicable laws of Pakistan, including the Emigration Ordinance, 1979 and the rules made under it. The Agent shall not hold themself out as a licensed Overseas Employment Promoter, or recruit or send any person abroad on their own account."),
  sub("The Agent shall not use the Company's name, logo or materials in any advertisement or social media post without the Company's prior written approval."),

  clause("Confidentiality"),
  sub("The Agent shall keep strictly confidential all non-public information about the Company, including its clients, overseas employers, partners, job orders, demand letters, rates, commission structures, processes and candidate data, and shall not disclose or use it except to perform this Agreement."),
  sub("Candidates' personal data and documents shall be handled securely and used only for the Company's purposes. These obligations shall continue after this Agreement ends."),

  clause("Non-Circumvention"),
  sub("During this Agreement and for twelve (12) months after it ends, the Agent shall not, directly or through any other person or agency, bypass the Company to deal with any client, overseas employer, partner or OEP introduced through the Company, or divert any candidate registered with the Company to any other agency."),

  clause("Term and Termination"),
  sub("This Agreement shall take effect on the Effective Date and continue until terminated by either Party."),
  sub("Either Party may terminate this Agreement by giving fifteen (15) days' written notice to the other."),
  sub("The Company may terminate this Agreement immediately in case of a breach of the No Charges to Candidates, Conduct and Compliance or Confidentiality clauses, fraud, dishonesty, or any other material breach."),
  sub("Commission on Successful Cases referred before termination shall remain payable once full payment is received, except where this Agreement is terminated for the Agent's breach."),

  clause("Indemnity"),
  sub("The Agent shall be responsible for, and shall compensate the Company against, any loss, claim, penalty or damage arising from the Agent's breach of this Agreement, any money collected from candidates by the Agent, or any false statement or document provided by the Agent."),

  clause("General"),
  sub("Notices under this Agreement shall be given in writing and delivered by hand, courier or email to the address or email of the receiving Party on the Company's records."),
  sub("If any provision of this Agreement is found invalid or unenforceable, the remaining provisions shall continue in full force. The Agent may not assign or transfer this Agreement."),
  sub("Any change to the commission rates or other terms shall be valid only if made in writing by the Company and accepted by the Agent."),

  clause("Governing Law and Entire Agreement"),
  sub("This Agreement shall be governed by the laws of the Islamic Republic of Pakistan. Any dispute shall first be resolved amicably; failing which, it shall be referred to the competent courts at Rawalpindi."),
  sub("This Agreement constitutes the entire agreement between the Parties on its subject matter. The Agent confirms that they have read and understood this Agreement and sign it voluntarily."),

  new Paragraph({ spacing: { before: 280, after: 200 }, keepNext: true,
    children: [r("IN WITNESS WHEREOF, the Parties have signed this Agreement on the date first written above.")] }),
  sigBlock(
    ["For and on behalf of the Company", COMPANY, "", "Signature: ______________________", `Name: ${a.signatory.name}`, `Designation: ${a.signatory.designation}`, "Company Stamp:"],
    ["Agent", a.name, "", "Signature: ______________________", `CNIC: ${a.cnic}`, "Date: ___________________________"],
  ),
];

const doc = new Document({
  creator: COMPANY,
  title: `Agent Agreement - ${a.name}`,
  styles: { default: { document: { run: { font: FONT, size: 22 } } } },
  numbering: { config: [{ reference: "sub", levels: [{ level: 0, format: LevelFormat.LOWER_LETTER,
    text: "(%1)", alignment: AlignmentType.LEFT,
    style: { paragraph: { indent: { left: 720, hanging: 400 } } } }] }] },
  sections: [{
    properties: {
      titlePage: true,
      page: { margin: { top: 3500, bottom: 2400, left: MARGIN_X, right: MARGIN_X, header: 0, footer: 1750 } },
    },
    headers: { first: background("first.jpg"), default: background("cont.jpg") },
    footers: { first: footer, default: footer },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outFile, buf);
  console.log(`Wrote ${outFile}`);
});
