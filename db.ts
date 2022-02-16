// Copyright 2016-2018, Pulumi Corporation.  All rights reserved.

import * as gcp from "@pulumi/gcp";
import * as config from "./config";

// Provision a database for our Flask app.
export const instance = new gcp.sql.DatabaseInstance("web-db", {
    databaseVersion: "SQLSERVER_2019_STANDARD",
    rootPassword: config.dbPassword,
    name: "web-db",
    deletionProtection: false,
    settings: {
	tier: "db-custom-2-13312",
        /*ipConfiguration: {
            authorizedNetworks: [{ value: "0.0.0.0/0" }],
        },*/
    },
});

const database = new gcp.sql.Database("appdb", 
    {instance: instance.name, name: "appdb"});

// Create a user with the configured credentials for the Flask app to use.
/*const user = new gcp.sql.User("web-db-user", {
    instance: instance.name,
    name: config.dbUsername,
    password: config.dbPassword,
});*/

