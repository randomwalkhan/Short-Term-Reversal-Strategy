# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-06-12 14:50:07 EDT`
Last processed slot: `entry_1500`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO + DRAM`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry mode: `shadow-only`; `10:00 AM-12:00 PM ET` 5-minute scans still log candidates when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`, but they do not open positions
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -10%`
- Option entry liquidity gate: `open interest >= 110`, `volume >= 20`, `spread <= 14%`
- Option exit safety: stale option `lastPrice` may be shown for mark-to-market, but take-profit / stop-loss triggers require an executable quote from bid/ask or bid
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$27,308.25`
- Equity: `$27,308.25`
- Realized PnL: `$17,308.25`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-06-12)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  MPWR           93.75               32            0.92             10.21       1585.17                71.83         0.565            pass              0.730             53.5                           0.489                2.11             -0.353                                 ok            True                  False
  ASML           94.12               34            0.90             11.98       1894.35                60.86         0.515            pass              0.823             78.4                           0.740               15.58              1.326                                 ok            True                   True
  INTU           79.41               34            1.21              2.34        275.91               100.42         0.713            pass              0.419             62.5                           0.606              -22.67             -2.199 downtrend_blocked_slope_and_streak           False                  False
    MU           81.58               38            0.05              0.33        995.73               115.24         0.706            pass              0.596             98.8                           0.786               -3.87             -0.754                                 ok           False                  False
  AVGO           84.85               33            0.99              2.67        384.43                69.71         0.585            pass              0.508             55.5                           0.636              -17.00             -2.489            downtrend_blocked_slope           False                  False
  TEAM           85.29               34            1.57              0.98         88.78                85.01         0.550            pass              0.562             68.5                           0.589              -24.28             -2.630 downtrend_blocked_slope_and_streak           False                  False
  CSCO           93.75               32            0.48              0.41        121.65                43.07         0.547            pass              0.662             31.2                           0.348               -0.07             -0.470                                 ok           False                  False
  AAPL          100.00               10            1.71              3.55        294.11                23.83         0.530            pass              0.500             15.6                           0.453               -5.14             -0.826            downtrend_blocked_slope           False                  False
  CTAS          100.00                2            3.05              3.88        180.22                29.28         0.525            pass              0.512             19.7                           0.191                1.99              0.286                                 ok           False                  False
  CRWD           81.08               37            0.65              3.14        690.18                64.88         0.520            pass              0.461             66.9                           0.473              -12.16             -1.430 downtrend_blocked_slope_and_streak           False                  False
  WDAY           84.85               33            1.25              1.14        130.04                70.45         0.504            pass              0.544             70.4                           0.663              -18.02             -1.909 downtrend_blocked_slope_and_streak           False                  False
  ISRG           81.48               27            1.13              3.26        411.50                34.54         0.497 below_threshold              0.365             54.2                           0.611               -0.98              0.025                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et         slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-06-12T14:50:07.527766-04:00   entry_1500           entry_skipped                                                                                                                                                                                                                                                                                                                                          {"budget": 13654.13, "entry_cost": 15345.0, "reason": "insufficient_cash", "ticker": "ASML"}
2026-06-12T14:50:07.527766-04:00   entry_1500 entry_candidate_skipped                                                                                                                                                                               {"early_entry_score": 0.73, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 0.0, "option_spread_pct": 7.0, "option_volume": 1.0, "reason": "no_trade_low_option_liquidity", "ticker": "MPWR", "timing_score": 0.565}
2026-06-12T14:50:07.527766-04:00   entry_1500          timing_overlay                                                                                                                                                                                                                                                                                                                          {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-06-12", "training_samples": 5261, "window": 5}
2026-06-12T13:30:06.922165-04:00 data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                         {'saved': 93}
2026-06-11T16:00:02.840701-04:00  manage_1600                    exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "PAYX260717C00100000", "fill_price": 4.725, "pnl": -1417.5, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "PAYX"}
2026-06-11T15:10:05.901456-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-11T15:05:01.637462-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-11T15:00:05.308604-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-11T14:55:01.789795-04:00   entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-06-11T14:50:01.795515-04:00   entry_1500                   entry {"allocated_cash": 14175.0, "asset_type": "option", "contract_symbol": "PAYX260717C00100000", "contracts": 27, "early_entry_score": 0.758, "entry_mode": "regular", "entry_option_price": 5.25, "execution_mode": "option", "matched_signals": 22, "option_liquidity_status": "ok", "option_open_interest": 685.0, "option_spread_pct": 9.52, "option_volume": 131.0, "success_rate": 100.0, "ticker": "PAYX", "timing_score": 0.573}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260612145007)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260612145007)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260612145007)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260612145007)

</details>
