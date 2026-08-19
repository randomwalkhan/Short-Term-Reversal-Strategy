# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-19 15:35:04 EDT`
Last processed slot: `manage_1530`

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

- Cash: `$53,138.00`
- Equity: `$53,138.00`
- Realized PnL: `$43,138.00`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-19)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
    MU           83.33               36            0.77              5.07        938.59               104.10         0.694          pass              0.547             71.7                           0.654                4.58              0.970                       ok            True                  False
  ASML           84.21               19            2.61             32.93       1788.87                47.17         0.526          pass              0.263             12.9                           0.256                2.57              0.769                       ok            True                  False
  MNST           86.36               44            0.05              0.02         47.37               244.45         0.980          pass              0.751             94.3                           0.399              -49.72             -8.846  downtrend_blocked_slope           False                  False
  SHOP           97.62               42            0.12              0.12        146.53                85.84         0.705          pass              0.937             88.9                           0.486               18.74              1.063                       ok           False                  False
  DRAM           76.32               38            0.15              0.06         55.08                98.64         0.685          pass              0.539             94.6                           0.609                0.24              0.841                       ok           False                  False
  MCHP           86.84               38            0.79              0.43         78.00                73.04         0.610          pass              0.588             52.7                           0.412               -3.84             -0.212 downtrend_blocked_streak           False                  False
  SOXL           79.31               29            5.95              5.38        126.80               165.44         0.587          pass              0.297             37.4                           0.579              -13.21             -0.165                       ok           False                  False
   AEP           96.15               26            0.09              0.08        126.31                19.03         0.554          pass              0.830             89.3                           0.629               -0.90              0.069                       ok           False                  False
  AMAT           83.33               18            3.70             13.33        508.62                84.57         0.552          pass              0.276             26.1                           0.505               -9.39             -0.703  downtrend_blocked_slope           False                  False
   HON           76.92               13            2.31              3.69        226.13                37.29         0.529          pass              0.093              6.6                           0.204              -10.32             -0.983  downtrend_blocked_slope           False                  False
  CSCO           90.91               44            0.04              0.03        111.60                42.21         0.526          pass              0.832             96.3                           0.530               -8.35             -1.002  downtrend_blocked_slope           False                  False
  PCAR          100.00               36            0.20              0.18        127.94                28.21         0.521          pass              0.846             73.4                           0.580               -5.78             -0.416  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-08-19T11:30:46.509801-04:00 early_entry_1130 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-19T10:58:16.376316-04:00 early_entry_1055 early_entry_shadow {"contract_symbol": "ZS260918C00185000", "current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "entry_ask": 15.8, "entry_bid": 15.1, "entry_mode": "early", "entry_option_price": 15.45, "hypothetical_budget": 26569.0, "hypothetical_contracts": 17, "matched_signals": 41, "option_liquidity_status": "low_volume", "option_open_interest": 1626.0, "option_spread_pct": 4.53, "option_volume": 9.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.774, "shadow_only": true, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "top_candidates": [{"current_drop_pct": 0.61, "early_entry_score": 0.737, "early_reclaim_pct": 71.8, "matched_signals": 41, "recovery_stability_score": 0.774, "success_rate": 90.24, "ticker": "ZS", "timing_score": 0.482, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-19T10:25:26.675121-04:00 early_entry_1025 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T12:30:08.738941-04:00      manage_1230               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "ALNY260918C00220000", "fill_price": 17.8, "pnl": 6240.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 28.06, "ticker": "ALNY"}
2026-08-18T11:46:30.861767-04:00 early_entry_1145 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:55:01.557589-04:00 early_entry_1055 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:35:03.185404-04:00 early_entry_1035 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T10:33:08.530330-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-18T09:38:41.008763-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
2026-08-18T09:20:07.104993-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 93}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260819153504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260819153504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260819153504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260819153504)

</details>
