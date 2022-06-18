// Copyright 2019 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

'use strict';

function main() {
  // [START bigquery_query]
  // [START bigquery_client_default_credentials]
  // Import the Google Cloud client library using default credentials
  const {BigQuery} = require('@google-cloud/bigquery');
  const bigquery = new BigQuery();
  const credentials = {
  user: "postgres",
  host: "dbtcourse.cusssbraayvm.ap-southeast-2.rds.amazonaws.com",
  database: "postgres",
  password: "********",
  port: 5432,
};

  var pg = require('pg');
  require('pg-essential').patch(pg);
  // [END bigquery_client_default_credentials]
  async function query() {
    // Queries the U.S. given names dataset for the state of Texas.

    const query = `SELECT name as names
      FROM \`bigquery-public-data.usa_names.usa_1910_2013\`
      WHERE state = 'AR'
      `;

    // For all options, see https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query
    const options = {
      query: query,
      // Location must match that of the dataset(s) referenced in the query.
      location: 'US',
    };

    // Run the query as a job
    const [job] = await bigquery.createQueryJob(options);
    console.log(`Job ${job.id} started.`);

    // Wait for the query to finish
    const [rows] = await job.getQueryResults();



    let client;
  try {
    client = new pg.Client(credentials);
    await client.connect();
    await client.executeBulkInsertion(rows,["names"],"names");
  } catch (e) {
  console.error(e);
} finally {
  client.end();
}


    // Print the results
    console.log(rows.length);



  }
  // [END bigquery_query]
  query();
}
main(...process.argv.slice(2));
