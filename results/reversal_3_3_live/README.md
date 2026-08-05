# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:10:05 EDT`
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

- Cash: `$17,080.75`
- Equity: `$32,980.75`
- Realized PnL: `$23,480.75`
- Unrealized PnL: `$-500.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode         instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 15900.0          4.1           3.98      138.68        138.56          bid_ask_mid                       3.98                bid_ask_mid                    True          -500.0                  -3.05         83.33               24              0.68          24.5           25.32                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  LRCX           87.88               33            0.71              1.59        317.06                92.33         0.677          pass              0.637             68.8                           0.441               -1.20             -0.075                       ok            True                  False
  CTAS           90.48               21            1.31              1.87        202.85                37.77         0.586          pass              0.435              7.8                           0.097               -0.19             -0.117                       ok            True                  False
  PAYX          100.00               22            0.56              0.47        118.46                35.13         0.560          pass              0.781             81.7                           0.445                7.66              0.773                       ok            True                  False
   KDP           80.00               20            0.71              0.15         31.03                28.75         0.556          pass              0.269             48.8                           0.423                2.25              0.457                       ok            True                  False
  MSFT           80.56               36            0.82              2.82        491.60                57.86         0.547          pass              0.327             27.9                           0.210               25.22              3.068                       ok            True                  False
  CPRT           87.50               16            2.24              0.46         29.20                38.86         0.520          pass              0.307              5.0                           0.168                5.78              0.597                       ok            True                  False
  GILD           91.67               12            1.87              1.77        134.49                28.84         0.519          pass              0.428             17.3                           0.149                1.83              0.216                       ok            True                  False
  SOXL           80.56               36            0.16              0.16        139.83               182.46         0.863          pass              0.567             97.4                           0.682              -13.24             -1.669 downtrend_blocked_streak           False                  False
  DRAM           75.00               36            0.12              0.05         54.87               109.93         0.738          pass              0.538             97.0                           0.756               -5.10             -0.555 downtrend_blocked_streak           False                  False
  AMAT           91.67               36            0.10              0.36        546.46                87.24         0.708          pass              0.841             95.1                           0.660               -1.41             -0.250                       ok           False                  False
  MRVL           81.08               37            0.32              0.48        218.38               100.52         0.670          pass              0.550             91.4                           0.668                3.28              0.327                       ok           False                  False
  TMUS           85.71                7            2.60              3.23        175.83                55.59         0.647          pass              0.222              1.5                           0.161               -9.61             -0.456  downtrend_blocked_slope           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-05T10:10:05.726457-04:00 early_entry_1010      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:00:04.700543-04:00 early_entry_1000      early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T00:00:04.689271-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-04T15:10:06.388254-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:05:01.446900-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:00:05.343102-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:55:02.363501-04:00       entry_1500            slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:50:05.317970-04:00       entry_1500                   entry {"allocated_cash": 16400.0, "asset_type": "option", "contract_symbol": "PEP260918C00140000", "contracts": 40, "early_entry_score": 0.423, "entry_mode": "regular", "entry_option_price": 4.1, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 3513.0, "option_spread_pct": 4.88, "option_volume": 30.0, "success_rate": 83.33, "ticker": "PEP", "timing_score": 0.544}
2026-08-04T14:50:05.317970-04:00       entry_1500 entry_candidate_skipped                                                                                                                                                              {"early_entry_score": 0.728, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 5.0, "option_spread_pct": 29.49, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "ROP", "timing_score": 0.567}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805101005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805101005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805101005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805101005)

</details>
