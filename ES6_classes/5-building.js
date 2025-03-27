export default class Building {
  constructor(sqft) {
    if (this.constructor !== Building
      && this.constructor.prototype.evacuationWarningMessage
      === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }

    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
