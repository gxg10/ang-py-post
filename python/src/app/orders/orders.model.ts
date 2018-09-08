export class Orders {
    constructor(
        public id: number,
        public data: Date,
        public simbol: string,
        public side: number,
        public simbol_type: string,
        public piata: string,
        public internal_account: number,
        public volum: number,
        public pret: number,
        public order_no: number,
        public tip_ordin: string,
        public trader: string
    ) {}
}