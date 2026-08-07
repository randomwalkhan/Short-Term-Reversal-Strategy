# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-07 10:20:01 EDT`
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
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TMUS           88.24               34            0.59              0.74        179.65                57.01         0.602          pass              0.642             67.5                           0.748               -0.66             -0.135                                 ok            True                  False
    MU           80.65               31            2.36             14.56        875.23               110.38         0.580          pass              0.334             39.6                           0.302               -6.55              0.143                                 ok            True                  False
  GOOG           81.40               43            0.52              1.31        356.06                50.46         0.514          pass              0.409             40.1                           0.401               11.18              1.321                                 ok            True                  False
  INSM           66.67               15            2.86              2.65        131.41               110.04         0.728          pass              0.112              2.1                           0.061               20.43              1.458                                 ok           False                  False
  MRVL           81.08               37            0.08              0.12        210.49                99.17         0.664          pass              0.565             96.6                           0.464                8.31              1.850                                 ok           False                  False
  ALNY           86.49               37            0.87              1.32        215.55               128.30         0.617          pass              0.614             66.4                           0.525              -21.17             -3.060            downtrend_blocked_slope           False                  False
  INTC           85.37               41            0.11              0.08         99.78                86.24         0.612          pass              0.686             93.8                           0.465                7.99              1.467                                 ok           False                  False
   CSX           91.30               23            0.81              0.29         50.58                29.04         0.548          pass              0.551             35.9                           0.307               -5.52             -0.318 downtrend_blocked_slope_and_streak           False                  False
  DRAM           76.00               25            3.77              1.36         50.86               108.98         0.544          pass              0.236             27.3                           0.251               -6.95              0.270                                 ok           False                  False
 GOOGL           79.07               43            0.54              1.34        357.17                51.28         0.506          pass              0.370             39.8                           0.370               11.29              1.354                                 ok           False                  False
  MNST           75.00                4            2.35              1.55         93.50                25.09         0.505          pass              0.141             30.1                           0.205               -1.65             -0.310            downtrend_blocked_slope           False                  False
   PEP           81.82               33            0.12              0.12        138.39                22.07         0.501          pass              0.518             88.6                           0.793                1.20             -0.121                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-08-07T10:20:01.443231-04:00 early_entry_1020 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:20:01.443231-04:00      manage_1030               exit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              {"asset_type": "option", "contract_symbol": "INTC260918C00100000", "fill_price": 10.0575, "pnl": -1676.25, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "INTC"}
2026-08-07T10:15:06.143326-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:10:01.433730-04:00 early_entry_1010 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 37, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.748, "shadow_only": true, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "top_candidates": [{"current_drop_pct": 0.58, "early_entry_score": 0.726, "early_reclaim_pct": 84.8, "matched_signals": 37, "recovery_stability_score": 0.748, "success_rate": 89.19, "ticker": "ORLY", "timing_score": 0.465, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T10:05:05.478835-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-07T10:00:04.307079-04:00 early_entry_1000 early_entry_shadow {"contract_symbol": "ORLY260918C00093330", "current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "entry_ask": 3.8, "entry_bid": 2.6, "entry_mode": "early", "entry_option_price": 3.2, "hypothetical_budget": 8804.13, "hypothetical_contracts": 27, "matched_signals": 36, "option_liquidity_status": "low_volume,wide_spread", "option_open_interest": 254.0, "option_spread_pct": 37.5, "option_volume": 17.0, "reason": "shadow_option_failed_liquidity", "recovery_stability_score": 0.651, "shadow_only": true, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "top_candidates": [{"current_drop_pct": 0.71, "early_entry_score": 0.701, "early_reclaim_pct": 81.6, "matched_signals": 36, "recovery_stability_score": 0.651, "success_rate": 88.89, "ticker": "ORLY", "timing_score": 0.463, "trend_health_status": "ok"}], "trend_health_status": "ok", "would_enter": false}
2026-08-07T00:00:06.807009-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     {'saved': 93}
2026-08-06T15:10:06.321105-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:05:05.205099-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
2026-08-06T15:00:02.209761-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260807102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260807102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260807102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260807102001)

</details>
