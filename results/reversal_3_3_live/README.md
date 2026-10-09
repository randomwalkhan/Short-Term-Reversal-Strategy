# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-10-09 14:45:04 EDT`
Last processed slot: `manual`

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

- Cash: `$117,274.30`
- Equity: `$117,274.30`
- Realized PnL: `$107,274.30`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-10-09)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  CSCO     option         option CSCO261120C00115000     74          2026-10-08         2026-10-09         7.25       8.425 8695.0   16.206897 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  CTSH           92.86               28            1.27              0.53         59.78                46.57         0.517            pass              0.558             14.6                           0.124                3.35              0.315                                 ok            True                  False
  SOXL           86.67               30            2.10              2.10        141.62               115.52         0.638            pass              0.488             37.6                           0.373               -7.88              0.097           downtrend_blocked_streak           False                  False
  META           83.33               36            0.33              1.68        720.17                52.31         0.582            pass              0.467             48.7                           0.349               -4.41             -0.190           downtrend_blocked_streak           False                  False
  QCOM           88.89               27            1.15              1.41        175.40                56.70         0.579            pass              0.565             52.1                           0.588              -13.85             -1.049 downtrend_blocked_slope_and_streak           False                  False
  NFLX           70.59               17            1.58              0.79         71.23                35.32         0.537            pass              0.133             11.0                           0.218               -1.00              0.024                                 ok           False                  False
  INTC           88.57               35            1.62              1.22        106.56                69.62         0.522            pass              0.476              9.4                           0.239              -14.36             -1.213 downtrend_blocked_slope_and_streak           False                  False
  PAYX           81.40               43            0.09              0.06        104.43                40.01         0.513            pass              0.485             65.4                           0.453                2.96              0.414                                 ok           False                  False
  INTU           88.89               36            0.46              0.98        303.46                43.01         0.512            pass              0.651             63.1                           0.530               10.19              1.275                                 ok           False                  False
  AMAT           84.62               39            0.32              1.14        509.08                47.71         0.506            pass              0.564             65.7                           0.363                4.73              0.510                                 ok           False                  False
  MDLZ           93.55               31            0.04              0.02         60.66                17.90         0.505            pass              0.840             95.9                           0.832                1.55              0.225                                 ok           False                  False
  LRCX           83.33               42            0.10              0.23        320.49                52.42         0.501            pass              0.618             92.9                           0.532                1.60              0.234                                 ok           False                  False
   APP           80.00               35            1.25              2.45        279.07                50.21         0.477 below_threshold              0.247             10.8                           0.140              -10.98             -1.176 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   detail
2026-10-09T13:50:04.651779-04:00      manage_1400               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "CSCO261120C00115000", "fill_price": 8.425, "pnl": 8695.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 16.21, "ticker": "CSCO"}
2026-10-09T11:44:59.466753-04:00 early_entry_1140 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-10-09T00:00:06.171329-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {'saved': 91, 'empty': 2}
2026-10-08T15:10:05.020875-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-08T15:05:01.112949-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-08T15:00:06.627098-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-08T14:55:05.835089-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "already_processed"}
2026-10-08T14:50:01.159134-04:00       entry_1500              entry                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"allocated_cash": 53650.0, "asset_type": "option", "contract_symbol": "CSCO261120C00115000", "contracts": 74, "early_entry_score": 0.235, "entry_mode": "regular", "entry_option_price": 7.25, "execution_mode": "option", "matched_signals": 16, "option_liquidity_status": "ok", "option_open_interest": 4349.0, "option_spread_pct": 4.14, "option_volume": 201.0, "success_rate": 81.25, "ticker": "CSCO", "timing_score": 0.563}
2026-10-08T14:50:01.159134-04:00       entry_1500     timing_overlay                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"status": "cached", "threshold": 0.5, "trade_date_et": "2026-10-08", "training_samples": 5978, "window": 5}
2026-10-08T12:00:05.051219-04:00 early_entry_1200 early_entry_shadow {"contract_symbol": "CTSH261120C00057500", "current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "entry_ask": 3.7, "entry_bid": 3.4, "entry_mode": "early", "entry_option_price": 3.55, "hypothetical_budget": 54289.65, "hypothetical_contracts": 152, "matched_signals": 36, "option_liquidity_status": "low_open_interest,low_volume", "option_open_interest": 29.0, "option_spread_pct": 8.45, "option_volume": 3.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.751, "shadow_only": true, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "top_candidates": [{"current_drop_pct": 0.63, "early_entry_score": 0.858, "early_reclaim_pct": 84.8, "matched_signals": 36, "recovery_stability_score": 0.751, "success_rate": 94.44, "ticker": "CTSH", "timing_score": 0.449, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20261009144504)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20261009144504)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20261009144504)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20261009144504)

</details>
