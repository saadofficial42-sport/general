// Generates a salary/commission revision letter (.docx) on RS Links letterhead.
// Usage: node scripts/make-salary-letter.js contracts/<letter>.json [out.docx]
// The JSON holds the employee, old/new salary, commission rates and signatory.

const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, Header, ImageRun, Table, TableRow,
  TableCell, WidthType, BorderStyle, AlignmentType, ShadingType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom,
} = require("docx");

const COMPANY = "RS Links Consultants (Pvt.) Ltd.";
const BRAND = "0E6143";
const FONT = "Calibri";
const LETTERHEAD_DIR = path.join(__dirname, "..", "templates", "letterhead");

const inFile = process.argv[2];
if (!inFile) {
  console.error("Usage: node scripts/make-salary-letter.js <letter.json> [out.docx]");
  process.exit(1);
}
const L = JSON.parse(fs.readFileSync(inFile, "utf8"));
const outFile = process.argv[3] || inFile.replace(/\.json$/, ".docx");
const pkr = (n) => `PKR ${n.toLocaleString("en-US")}/-`;

const r = (text, opts = {}) => new TextRun({ text, font: FONT, size: 21, ...opts });
const b = (text, opts = {}) => r(text, { bold: true, ...opts });
const p = (children, opts = {}) => new Paragraph({
  children: (Array.isArray(children) ? children : [children]).map((c) => (typeof c === "string" ? r(c) : c)),
  spacing: { after: 110, line: 264 }, alignment: AlignmentType.JUSTIFIED, ...opts,
});

const background = new Header({ children: [new Paragraph({ children: [
  new ImageRun({ type: "jpg", data: fs.readFileSync(path.join(LETTERHEAD_DIR, "first.jpg")),
    transformation: { width: 795, height: 1124 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 },
      behindDocument: true, allowOverlap: true,
    } }),
] })] });

const MARGIN_X = 1000;
const W = 11906 - 2 * MARGIN_X;
const border = { style: BorderStyle.SINGLE, size: 4, color: "B8D4C7" };
const borders = { top: border, bottom: border, left: border, right: border };
const cell = (child, w, shade) => new TableCell({ width: { size: w, type: WidthType.DXA }, borders,
  ...(shade ? { shading: { type: ShadingType.CLEAR, fill: "E8F3EE", color: "auto" } } : {}),
  margins: { top: 30, bottom: 30, left: 120, right: 120 },
  children: [new Paragraph({ keepNext: true, children: [child] })] });
const TW = W - 720;
const COLS = [TW - 3200, 3200];
const commissionTable = new Table({
  width: { size: TW, type: WidthType.DXA }, columnWidths: COLS, indent: { size: 720, type: WidthType.DXA },
  rows: [
    new TableRow({ children: [cell(b("Destination"), COLS[0], true), cell(b("Commission per approved case"), COLS[1], true)] }),
    ...L.commission.map(([dest, amt]) => new TableRow({ cantSplit: true, children: [
      cell(r(dest), COLS[0]), cell(b(pkr(amt)), COLS[1])] })),
  ],
});

const item = (n, children) => new Paragraph({
  children: [b(`${n}.  `, { color: BRAND }), ...children.map((c) => (typeof c === "string" ? r(c) : c))],
  indent: { left: 360, hanging: 360 }, spacing: { after: 100, line: 276 }, alignment: AlignmentType.JUSTIFIED,
});

const sig = (lines) => lines.map((l, i) => new Paragraph({ spacing: { after: 40 }, keepNext: true,
  children: [i === 0 ? b(l) : r(l)] }));

const body = [
  new Paragraph({ spacing: { after: 0 }, children: [b(`${L.salutation} ${L.name}`)] }),
  new Paragraph({ spacing: { after: 0 }, children: [r(L.designation)] }),
  new Paragraph({ spacing: { after: 160 }, children: [r(COMPANY)] }),
  p([b("Subject: ", { color: BRAND }), b("Revision of Basic Salary and Commission Structure")], { spacing: { after: 140 } }),
  p(`Dear ${L.salutation} ${L.name.split(" ").slice(-1)[0]},`),
  p(["We are pleased to inform you that, in recognition of your performance and contribution to the Company, the management has approved a revision of your remuneration with effect from ",
    b(L.effectiveDate), " as follows:"]),
  item(1, [b("Basic Salary: "), "Your basic salary has been increased by ", b(pkr(L.newSalary - L.oldSalary)),
    `, from ${pkr(L.oldSalary)} to `, b(pkr(L.newSalary)), ` (${L.newSalaryWords} only) per month, disbursed within the first week of every calendar month.`]),
  item(2, [b("Commission: "), "Your commission for every approved case submitted will be as follows. Commission will continue to become payable only after the Company has received full payment for the relevant case from the candidate and/or client, in accordance with your Employment Agreement."]),
  commissionTable,
  new Paragraph({ spacing: { after: 80 }, children: [] }),
  p("This letter forms part of, and amends, your Employment Agreement with the Company. All other terms and conditions of your Employment Agreement remain unchanged and in full force."),
  p("We appreciate your efforts and look forward to your continued commitment and contribution to the growth of the Company."),
  p("Yours sincerely,", { spacing: { before: 60, after: 420 }, keepNext: true }),
  ...sig(["______________________________", L.signatory.name, L.signatory.designation, `For and on behalf of ${COMPANY}`]),
  new Paragraph({
    spacing: { before: 220, after: 80 }, keepNext: true,
    border: { top: { style: BorderStyle.DASHED, size: 6, color: "9BB8AA", space: 8 } },
    children: [b("ACKNOWLEDGEMENT", { color: BRAND, size: 20 })],
  }),
  p(`I, ${L.name}, CNIC No. ${L.cnic}, acknowledge receipt of this letter and accept the revised terms stated above.`, { keepNext: true }),
  new Paragraph({ spacing: { before: 200 }, children: [r("Signature: ______________________          Date: ______________________")] }),
];

const doc = new Document({
  creator: COMPANY,
  title: `Salary Revision - ${L.name}`,
  styles: { default: { document: { run: { font: FONT, size: 21 } } } },
  sections: [{
    properties: { page: { margin: { top: 3450, bottom: 2250, left: MARGIN_X, right: MARGIN_X, header: 0, footer: 0 } } },
    headers: { default: background },
    children: body,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  fs.writeFileSync(outFile, buf);
  console.log(`Wrote ${outFile}`);
});
