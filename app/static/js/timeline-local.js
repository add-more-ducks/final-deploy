const options = {
  language: 'en',
};
//
// load the data from a local csv
//

const csvData = {
  events: [],
};

d3.csv('app/static/js/timeline-data.csv', (error, data) => {
  data.forEach((itemData) => {
        // reference for json format: https://timeline.knightlab.com/docs/json-format.html
        // inspired from https://github.com/NUKnightLab/TimelineJS3/blob/master/source/js/core/TL.ConfigFactory.js
    // console.log(itemData);
    const event = {
      start_date: TL.Date.parseDate(itemData.date),
      media:
      {
        caption: itemData.mediaCaption || '',
        credit: itemData.mediaCredit || '',
        url: itemData.mediaUrl || '',
        thumbnail: itemData.mediaThumbnail || '',
      },
      text:
      {
        headline: itemData.titre || '',
        text: itemData.texte || '',
      },
      background: {
        url: itemData.backgroundUrl || '',
        color: itemData.backgroundColor || '',
      },
    };

    if (itemData.type === 'title') {
      if (!csvData.title) {
        csvData.title = event;
      } else {
        console.log('Multiple title slides detected.');
        csvData.events.push(event);
      }
    } else {
      csvData.events.push(event);
    }
  });
  // console.log(csvData);
  const timeline = new TL.Timeline('timeline', csvData, options);
});
