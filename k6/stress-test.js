import http from 'k6/http';
import { check } from 'k6';
import { htmlReport } from 'https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js';

const BASE_URL = 'https://taylor-swift-api.sarbo.workers.dev';
const REPORT_HTML_FILE = '/reports/stress-summary.html';

//teste de estresse gradual que vai subindo ate 150 usuarios e dps desce pra 0
export const options = {
  stages: [
    { duration: '10s', target: 5 }, //50
    { duration: '10s', target: 10 }, //100
    { duration: '10s', target: 15 }, //150
    { duration: '10s', target: 0 },
  ],
  gracefulRampDown: '5s',
};

export default function () {

  const albumsResponse = http.get(`${BASE_URL}/albums`);
  check(albumsResponse, { 'get albums status 200': (response) => response.status === 200 });

  const songsResponse = http.get(`${BASE_URL}/songs`);
  check(songsResponse, { 'get songs status 200': (response) => response.status === 200 });

  const lyricsResponse = http.get(`${BASE_URL}/lyrics?shouldRandomizeLyrics=true&numberOfParagraphs=1`);
  check(lyricsResponse, { 'get lyrics status 200': (response) => response.status === 200 });

}

export function handleSummary(data) {
  return {
    [REPORT_HTML_FILE]: htmlReport(data),
  };
}