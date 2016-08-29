CREATE TABLE "Transaction" (
	"Id" CHAR(36) NOT NULL,
	"Account.Id" VARCHAR(20) NOT NULL,
	"Description.Id" VARCHAR(50) NOT NULL,
	"Amount" DECIMAL(13,2) NOT NULL,
	"Date" DATE NOT NULL,
	"Balance" DECIMAL(13,2) NOT NULL,
	PRIMARY KEY("Id"), 
	FOREIGN KEY("Account.Id") REFERENCES "Account"("Id"),
	FOREIGN KEY("Description.Id") REFERENCES "Description"("Id")
);

CREATE TABLE "Description" (
	 "Id" VARCHAR(50) NOT NULL, 
	 "Category.Id" VARCHAR(20) NOT NULL, 
	 PRIMARY KEY("Id"), 
	 FOREIGN KEY ("Category.Id") REFERENCES "Category"("Id")
 );

CREATE TABLE "Category" ( 
	"Id" VARCHAR(20) NOT NULL, 
	"Detail" VARCHAR(20) NOT NULL, 
	PRIMARY KEY("Id")
);

CREATE TABLE "Type" ( 
	"Id" VARCHAR(20) NOT NULL, 
	"Description" VARCHAR(30), 
	PRIMARY KEY ("Id")
);

CREATE TABLE "Account" ( 
	"Id" VARCHAR(20) NOT NULL, 
	"Description" VARCHAR(30) NOT NULL, 
	PRIMARY KEY("Id") 
);