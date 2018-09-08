export class Customer {
    constructor(
        public firstname: string,
        public lastname: string,
        public age: number,
        public createdAt: Date,
        public updatedAt: Date,
        public _id?: number,
    ) {}
}