// Time = 0(1) for subscribe and release and 0(N) for emit
// Space = 0(N)

class EventEmitter {
  subscriptions = new Map();

  subscribe(eventName, callback) {
    if (!this.subscriptions.has(eventName)) {
      this.subscriptions.set(eventName, new Set()); //  same callback could subscribe // on same event multiple times
    }
    const subscriptions = this.subscriptions.get(eventName);
    const callbackObj = { callback }; // map can only store both objects and primitive values ( string, number, bigint, boolean, undefined, symbol, and null)
    subscriptions.add(callbackObj);

    return {
      release: () => {
        subscriptions.delete(callbackObj);
        // edge case if there is no more call back in event subscription
        if (subscriptions.size === 0) {
          this.subscriptions.delete(eventName);
        }
      },
    };
  }

  emit(eventName, ...args) {
    const subscriptions = this.subscriptions.get(eventName);
    if (subscriptions) {
      subscriptions.forEach((cbObj) => {
        cbObj.callback.apply(this, args);
      });
    }
  }
}
