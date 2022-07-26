

function sumOfMSizedSubArraysWithEqualsToD(s: number[], d: number, m: number): number {
    function recursiveCombinator( 
        ss: number[], 
        startIndex: number, 
        d : number, 
        m : number, 
        currentSum: number ):number{
        if ( m == 0){
            if ( d == currentSum) return 1;
            else return 0;
        }   
        let result = 0

        for ( let i = startIndex; i < ss.length ; i++ ){
            let newSum = currentSum + s[i];    
            result += recursiveCombinator(s, i+1, d, m-1,newSum );
        }
        return result;
    }
    return recursiveCombinator( s,0,d,m,0);
}
