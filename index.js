const functions = require("firebase-functions");
const puppeteer = require("puppeteer");
const Crawler = require("./crawler");
const Firestore = require("./firebasestore");
const constraint = require("./crawler/constraint");
const COLLECTION_NAME = 'rows1';
const rowsCol = new Firestore(COLLECTION_NAME);
// Error =  "Possible EventEmitter memory leak detected. 11 SIGINT listeners added" solutions
process.setMaxListeners(Infinity);
exports.betaRowListener = functions.firestore
  .document(`${COLLECTION_NAME}/{userId}`)
  .onCreate(async (snap, context) => {
    const browser = await puppeteer.launch({ args: ["--no-sandbox"] });
    const page = await browser.newPage();
    const data = snap.data();
    const crawler = new Crawler(data.stage, page, data.url, 2);
    if (!crawler.stage) {
      console.log(data);
      return 0;
    }
  });
