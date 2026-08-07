# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:30:01 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$32,694.50`
- Equity: `$32,694.50`
- Realized PnL: `$22,694.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-08-07)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price      pnl  return_pct           exit_reason
  INTC     option         option INTC260918C00100000     15          2026-08-06         2026-08-07       11.175     10.0575 -1676.25       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
    MU           82.76               29            2.62             16.20        874.53               110.38         0.578            pass              0.357             32.8                           0.339               -6.80              0.130                                 ok            True                  False
  INSM           64.29               14            2.93              2.72        131.39               110.04         0.726            pass              0.110              3.7                           0.071               20.34              1.455                                 ok           False                  False
  ALNY           86.49               37            0.86              1.31        215.56               128.30         0.618            pass              0.615             66.9                           0.511              -21.16             -3.060            downtrend_blocked_slope           False                  False
  TMUS           89.19               37            0.40              0.50        179.75                57.01         0.597            pass              0.718             77.9                           0.785               -0.47             -0.126                                 ok           False                  False
   CSX           91.30               23            0.79              0.28         50.58                29.04         0.549            pass              0.555             37.5                           0.307               -5.50             -0.317 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.00               25            3.93              1.41         50.83               108.98         0.533            pass              0.226             24.3                           0.305               -7.11              0.263                                 ok           False                  False
   MAR           93.75               32            0.53              1.32        359.10                38.09         0.523            pass              0.744             59.5                           0.334               -4.45             -0.851 downtrend_blocked_slope_and_streak           False                  False
   PEP           81.82               33            0.09              0.09        138.40                22.07         0.503            pass              0.525             91.0                           0.774                1.22             -0.119                                 ok           False                  False
 GOOGL           80.00               45            0.48              1.21        357.23                51.28         0.498 below_threshold              0.387             45.6                           0.401               11.35              1.357                                 ok           False                  False
  GOOG           82.98               47            0.44              1.10        356.15                50.46         0.495 below_threshold              0.478             49.7                           0.446               11.27              1.325                                 ok           False                  False
  PCAR           97.50               40            0.06              0.06        132.04                29.35         0.491 below_threshold              0.928             93.0                           0.477               -0.20             -0.128                                 ok           False                  False
  CHTR           90.48               21            2.34              2.58        156.33                48.50         0.480 below_threshold              0.498             32.3                           0.309               24.69              2.010                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-08-07T10:30:01.589091-04:00 early_entry_1030 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:25:02.606392-04:00 early_entry_1025 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "entry_ask": 3.7, "entry_bid": 2.95, "entry_mode": "early", "entry_option_price": 3.325, "hypothetical_budget": 16347.25, "hypothetical_contracts": 49, "matched_signals": 38, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 22.56, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.808, "shadow_only": true, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "top_candidates": [{"current_drop_pct": 0.5, "early_entry_score": 0.746, "early_reclaim_pct": 86.9, "matched_signals": 38, "recovery_stability_score": 0.808, "success_rate": 89.47, "ticker": "ORLY", "timing_score": 0.464, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:20:01.443231-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:20:01.443231-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "INTC260918C00100000", "fill_price": 10.0575, "pnl": -1676.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "INTC"}
2026-08-07T10:15:06.143326-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:10:01.433730-04:00 early_entry_1010 early_entry_shadow    {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:05:05.478835-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow    {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        {'saved': 93}
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807103001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807103001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807103001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807103001)

</details>
