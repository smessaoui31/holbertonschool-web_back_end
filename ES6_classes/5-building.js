import Building from './5-building.js';

class TestBuilding extends Building {
  evacuationWarningMessage() {
    return 'Evacuate immediately!';
  }
}

const b1 = new TestBuilding(200);
console.log(b1.sqft); // 200
console.log(b1.evacuationWarningMessage());

class BrokenBuilding extends Building {}

try {
  const b2 = new BrokenBuilding(100);
} catch (err) {
  console.log(err.message);
}
