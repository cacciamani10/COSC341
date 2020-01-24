const {
    change, stripQuotes, scramble, say, powers, interleave,
  } = require('./h2');
  
  // Helper for the scramble tests
  function anagramsOfEachOther(s, t) {
    return s.split('').sort().join('') === t.split('').sort().join('');
  }
  
  // Helper for testing the callbacky problems
  function generatorToArray(generator, ...args) {
    const result = [];
    generator(...args, (item) => result.push(item));
    return result;
  }
  
  describe('change', () => {
    it('handles zero', () => {
      expect(change(0)).toEqual([0, 0, 0, 0]);
    });
  
    it('computes answers for small integer values fine', () => {
      expect(change(97)).toEqual([3, 2, 0, 2]);
      expect(change(8)).toEqual([0, 0, 1, 3]);
      expect(change(250)).toEqual([10, 0, 0, 0]);
      expect(change(144)).toEqual([5, 1, 1, 4]);
      expect(change(97)).toEqual([3, 2, 0, 2]);
    });
  
    it('handles large values', () => {
      // This test only passes if the solution is efficient
      expect(change(100000000000)).toEqual([4000000000, 0, 0, 0]);
    });
  
    it('throws the proper exception for negative arguments', () => {
      expect(() => change(-50)).toThrow(RangeError);
    });
  });
  
  describe('stripQuotes', () => {
    it('works on the empty string', () => {
      expect(stripQuotes('')).toEqual('');
    });
  
    it('strips quotes properly for non-empty strings', () => {
      expect(stripQuotes('Hello, world')).toEqual('Hello, world');
      expect(stripQuotes('"\'')).toEqual('');
      expect(stripQuotes('a"""\'\'"z')).toEqual('az');
    });
  });
  
  describe('scramble', () => {
    it('scrambles properly', () => {
      ['a', 'rat', 'JavaScript testing', '', 'zzz', '^*^*)^▱ÄÈËɡɳɷ'].forEach((s) => {
        expect(anagramsOfEachOther(s, scramble(s))).toBeTruthy();
      });
    });
  
    it('is really random (produces all permutations)', () => {
      const possibilities = new Set('ABC ACB BAC BCA CAB CBA'.split(' '));
      for (let i = 0; i < 200; i += 1) {
        possibilities.delete(scramble('ABC'));
      }
      expect(possibilities.size).toBe(0);
    });
  });
  
  describe('say', () => {
    it('works when there are no words', () => {
      expect(say()).toBe('');
    });
  
    it('works when there are words', () => {
      expect(say('hi')()).toBe('hi');
      expect(say('hi')('there')()).toBe('hi there');
      expect(say('hello')('my')('name')('is')('Colette')()).toBe('hello my name is Colette');
    });
  });
  
  describe('powers', () => {
    it('generates sequences of powers properly', () => {
      expect(generatorToArray(powers, 2, -5)).toEqual([]);
      expect(generatorToArray(powers, 7, 0)).toEqual([]);
      expect(generatorToArray(powers, 3, 1)).toEqual([1]);
      expect(generatorToArray(powers, 2, 63)).toEqual([1, 2, 4, 8, 16, 32]);
      expect(generatorToArray(powers, 2, 64)).toEqual([1, 2, 4, 8, 16, 32, 64]);
    });
  });
  
  
  
  describe('interleave', () => {
    it('interleaves properly', () => {
      expect(interleave([])).toEqual([]);
      expect(interleave([1, 4, 6])).toEqual([1, 4, 6]);
      expect(interleave([], 2, 3)).toEqual([2, 3]);
      expect(interleave([1], 9)).toEqual([1, 9]);
      expect(interleave([8, 8, 3, 9], 1)).toEqual([8, 1, 8, 3, 9]);
      expect(interleave([2], 7, '8', {})).toEqual([2, 7, '8', {}]);
    });
  });
  