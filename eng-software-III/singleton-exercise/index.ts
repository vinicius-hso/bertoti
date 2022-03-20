//* singleton pattern

class DatabaseConfig {
  public dbName: string;
  public dbPassword: string;
  public dbPort: number;
  public sgbd: string;

  private static instance: DatabaseConfig;

  private constructor(
    dbName: string,
    dbPassword: string,
    dbPort: number,
    sgbd: string
  ) {
    this.dbName = dbName;
    this.dbPassword = dbPassword;
    this.dbPort = dbPort;
    this.sgbd = sgbd;
  }

  public static getInstance(
    dbName: string,
    dbPassword: string,
    dbPort: number,
    sgbd: string
  ): DatabaseConfig {
    if (!this.instance) {
      this.instance = new DatabaseConfig(dbName, dbPassword, dbPort, sgbd);
    }
    return this.instance;
  }
}

const dbConfig1: DatabaseConfig = DatabaseConfig.getInstance(
  "db-singleton1",
  "123456",
  3333,
  "PostgreSQL"
);

const dbConfig2: DatabaseConfig = DatabaseConfig.getInstance(
  "db-singleton2",
  "654321",
  3000,
  "MySQL"
);

console.log(dbConfig1);
console.log(dbConfig2);
