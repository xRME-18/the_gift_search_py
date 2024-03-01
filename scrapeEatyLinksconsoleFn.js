function downloadEtsyLinks(pageNumber) {
  // Select all anchor elements with the class "listing-link"
  const links = document.querySelectorAll("a.listing-link");

  // Map over the NodeList to extract href attributes
  const hrefs = Array.from(links).map((link) => ({ href: link.href }));

  // Convert the array of objects to a JSON string
  const json = JSON.stringify(hrefs, null, 2); // The '2' argument here adds indentation to the JSON

  // Create a Blob from the JSON string
  const blob = new Blob([json], { type: "application/json" });

  // Create a link element
  const downloadLink = document.createElement("a");

  // Create a URL for the blob
  const url = URL.createObjectURL(blob);

  // Set the download attribute on the link to the filename you want to use
  downloadLink.download = `etsy-links${pageNumber}.json`;

  // Set the href to the blob URL
  downloadLink.href = url;

  // Append the link to the document so it can be clicked
  document.body.appendChild(downloadLink);

  // Programmatically click the link to trigger the download
  downloadLink.click();

  // Clean up by revoking the object URL and removing the link element
  URL.revokeObjectURL(url);
  downloadLink.remove();
}

// Call the function to download Etsy links
downloadEtsyLinks();
