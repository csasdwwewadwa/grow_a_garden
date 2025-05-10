function formallize(str) {
  return str
  .split("_")
  .filter(word => word.length > 0) // handle multiple underscores
  .map(word => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
  .join(" ");
}

const listSections = document.querySelectorAll('.list-section');

const sectionMap = {
  'list-section-seeds': ''
}

fetch('data/buyable_items_selected.json')
  .then(response => response.json())
  .then(data => {
    const itemsData = data.items;
    const itemsDataSeeds = itemsData.seeds
    const itemsDataGears = itemsData.gears
    const itemsDataEggs = itemsData.eggs

    const seedsList = document.getElementById('itemListBuyingSeeds')
    const gearsList = document.getElementById('itemListBuyingGears')
    const eggsList = document.getElementById('itemListBuyingEggs')

    itemsDataSeeds.selected.forEach(raw_name => {
      const listItem = document.createElement('li')
      listItem.textContent = formallize(raw_name)
      if (itemsDataSeeds.selected_alt_buy.includes(raw_name)) {
        listItem.add('selected-alt-buy')
      }
      seedsList.appendChild(listItem)
    });
  })
  .catch(error => {
    console.error('Error loading JSON:', error);
    const myList = document.getElementById('myList');
    myList.textContent = "Error loading data.";
  });