//* singleton pattern
var DatabaseConfig = /** @class */ (function () {
    function DatabaseConfig(dbName, dbPassword, dbPort, sgbd) {
        this.dbName = dbName;
        this.dbPassword = dbPassword;
        this.dbPort = dbPort;
        this.sgbd = sgbd;
    }
    DatabaseConfig.getInstance = function (dbName, dbPassword, dbPort, sgbd) {
        if (!this.instance) {
            this.instance = new DatabaseConfig(dbName, dbPassword, dbPort, sgbd);
        }
        return this.instance;
    };
    return DatabaseConfig;
}());
var dbConfig1 = DatabaseConfig.getInstance("db-singleton1", "123456", 3333, "PostgreSQL");
var dbConfig2 = DatabaseConfig.getInstance("db-singleton2", "654321", 3000, "MySQL");
console.log(dbConfig1);
console.log(dbConfig2);
