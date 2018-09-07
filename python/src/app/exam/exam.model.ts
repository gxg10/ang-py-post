export class Exam {
    constructor(
        public title: string,
        public description: string,
        public _id?: number,
        public updateAt?: Date,
        public createdAt?: Date,
        public lastUpdatedBy?:string,
    ) {}
}