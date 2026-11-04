# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-11-04 10:10:06 EST`
Last processed slot: `manage_1000`

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

- Cash: `$129,631.55`
- Equity: `$129,631.55`
- Realized PnL: `$119,631.55`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-11-04)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  SOXL           73.33               30            1.64              0.84         72.76               167.58         0.763            pass              0.448             79.5                           0.605              -30.34             -2.901            downtrend_blocked_slope           False                  False
  INTC           73.33               30            2.04              0.86         60.18               129.60         0.760            pass              0.363             51.4                           0.515              -36.19             -4.906            downtrend_blocked_slope           False                  False
  DRAM           73.08               26            1.19              0.40         47.47                69.30         0.611            pass              0.371             67.7                           0.561               -4.24             -0.078                                 ok           False                  False
  REGN           73.91               23            1.37              9.34        969.36                48.26         0.529            pass              0.140              0.0                           0.157               19.16              2.163                                 ok           False                  False
  ASML           75.00               16            2.07             22.50       1542.50                44.05         0.515            pass              0.198             35.5                           0.476               -9.23             -0.536            downtrend_blocked_slope           False                  False
  MPWR           60.87               23            1.62             15.02       1321.86                60.85         0.513            pass              0.291             51.0                           0.374                1.83              0.846                                 ok           False                  False
  KLAC           72.50               40            0.32              0.35        156.05                57.09         0.512            pass              0.514             87.7                           0.751               -4.73              0.298                                 ok           False                  False
  AMAT           68.29               41            0.19              0.51        381.70                58.39         0.511            pass              0.534             94.2                           0.769               -6.79             -0.209                                 ok           False                  False
  AVGO           77.50               40            0.12              0.28        332.01                44.04         0.506            pass              0.533             94.0                           0.729               -1.80              0.011                                 ok           False                  False
    MU           73.91               23            2.21             13.25        849.42                64.24         0.504            pass              0.288             50.2                           0.518               -8.48             -0.582            downtrend_blocked_slope           False                  False
  NVDA           76.00               25            0.66              0.95        206.28                32.59         0.501            pass              0.379             76.3                           0.669               -7.50             -0.684 downtrend_blocked_slope_and_streak           False                  False
   BKR           66.67                6            3.10              1.14         52.30                46.45         0.498 below_threshold              0.134             28.0                           0.328               -8.65             -0.706            downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                detail
2026-11-04T10:10:06.483796-05:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:05:05.606953-05:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T10:00:05.152440-05:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                 {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-11-04T09:20:05.283761-05:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                             {'saved': 91, 'empty': 2}
2026-11-03T16:10:06.665587-05:00      manage_1600               exit                                                                                                                                                                                                                                                     {"asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "fill_price": 1.305, "pnl": -6815.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MDLZ"}
2026-11-03T15:10:05.032509-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:05:04.979432-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T15:00:05.978517-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:55:04.978613-05:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                       {"reason": "already_processed"}
2026-11-03T14:50:06.793337-05:00       entry_1500              entry {"allocated_cash": 68150.0, "asset_type": "option", "contract_symbol": "MDLZ261218C00067500", "contracts": 470, "early_entry_score": 0.508, "entry_mode": "regular", "entry_option_price": 1.45, "execution_mode": "option", "matched_signals": 11, "option_liquidity_status": "ok", "option_open_interest": 1121.0, "option_spread_pct": 6.9, "option_volume": 33.0, "success_rate": 90.91, "ticker": "MDLZ", "timing_score": 0.603}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261104101006)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261104101006)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261104101006)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261104101006)

</details>
