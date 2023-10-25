function csvToMarkdown(csvString) {
    const lines = csvString.trim().split('\n');
    const [header, ...data] = lines.map(line => line.split(',').map(cell => cell.trim()));
  
    const numColumns = header.length;
  
    let markdownTable = `| ${header.join(' | ')} |\n`;
    markdownTable += `| ${Array(numColumns).fill(':---:').join(' | ')} |\n`;
  
    for (const row of data) {
      if (row.some(cell => cell.trim() !== '')) {
        markdownTable += `| ${row.join(' | ')} |\n`;
      }
    }
  
    return markdownTable;
  }
  
  const csvString = `
  name, item, number
  jay, bird, 1
  crow, bird, 2
  `;
  
  const markdownTable = csvToMarkdown(csvString);
  console.log(markdownTable);
  