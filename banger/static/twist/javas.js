async function balance() {
    try {
        const response = await fetch("/twist/fet/balance");
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const data = await response.json();
        document.getElementById("balance").textContent = data.balance;
    } catch (error) {
        console.error("Fetch error:", error);
    }
};

async function loaditemstable(location) {
    try {
        const response = await fetch(`/twist/fet/${location}`);
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }

        const tableHTML = await response.text(); 
        document.getElementById(`${location}`).innerHTML = tableHTML;  

    } catch (error) {
        console.error("Fetch error:", error);
    }
    if (location == "inventory"){
        const deckbuilder = document.getElementsByClassName("deckbuilder");
        const deckbuilderA = document.getElementsByClassName("deckbuilderA");

        for (let i = 0; i < deckbuilder.length; i++) {
        deckbuilder[i].style.display = "none";
        }
        for (let i = 0; i < deckbuilderA.length; i++) {
        deckbuilderA[i].style.display = "none";
        }
    }
}

let globalData = null
async function deckshow() {
    try {
        const response = await fetch("/twist/fet/decktab");
        if (!response.ok) {
            throw new Error(`HTTP error: ${response.status}`);
        }
        globalData = await response.json();
        showDeck('deck1');
    } catch (error) {
        console.error("Fetch error:", error);
    }
};

function showDeck(deck) {

    const decknumber = deck

    const deckname = globalData[deck].name
    const Value1 = globalData[deck].slot1;
    const Value2 = globalData[deck].slot2;
    const ValueA= globalData[deck].slotA;
    const Value3 = globalData[deck].slot3;
    const Value4 = globalData[deck].slot4;

    const decknameslot = document.getElementById("deckname")
    const decknumberslot = document.getElementById("decknumber")
    const slot1 = document.getElementById("slot1");
    const slot2 = document.getElementById("slot2");
    const slotA = document.getElementById("slotA");
    const slot3 = document.getElementById("slot3");
    const slot4 = document.getElementById("slot4");
    
    slot1.alt = Value1;
    slot2.alt = Value2;
    slotA.alt = ValueA;
    slot3.alt = Value3;
    slot4.alt = Value4;
    decknameslot.textContent = deckname
    decknumberslot.textContent = decknumber
    
    // Optionally set an image source if needed
    // img.src = `/static/cards/${cardValue}.png`;
}
