# Reversal 3.5 Live Paper Test

Latest checkpoint (ET): `2026-08-05 10:15:01 EDT`
Last processed slot: `early_entry_1015`

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
   PEP     option         option PEP260918C00140000       2026-08-04                   1     40     16400.0                 15900.0          4.1           3.98      138.68        138.29          bid_ask_mid                       3.98                bid_ask_mid                    True          -500.0                  -3.05         83.33               24              0.68          24.5            25.9                  26.13                3513.0           30.0               0.05                      ok
```

## Today's Closed Trades (2026-08-05)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day      trend_health_status  call_candidate  early_entry_candidate
  LRCX           88.89               36            0.56              1.24        317.21                92.33         0.670          pass              0.705             75.7                           0.435               -1.04             -0.068                       ok            True                  False
  MDLZ           95.24               21            0.66              0.29         61.96                31.68         0.588          pass              0.659             42.3                           0.405                1.33              0.292                       ok            True                  False
  CTAS           90.91               22            1.17              1.66        202.94                37.77         0.588          pass              0.488             19.5                           0.268               -0.04             -0.111                       ok            True                  False
   PEP           83.33               24            0.60              0.58        138.85                25.68         0.552          pass              0.326             29.7                           0.311                1.93              0.236                       ok            True                  False
  MSFT           81.08               37            0.73              2.51        491.74                57.86         0.547          pass              0.372             36.1                           0.313               25.33              3.072                       ok            True                  False
   TRI           86.11               36            0.96              0.73        108.84                67.97         0.512          pass              0.568             60.1                           0.381               23.79              2.143                       ok            True                  False
  CPRT           85.00               20            1.92              0.40         29.23                38.86         0.510          pass              0.307             18.7                           0.214                6.13              0.612                       ok            True                  False
  SOXL           80.56               36            0.58              0.57        139.66               182.46         0.847          pass              0.544             90.4                           0.621              -13.61             -1.688 downtrend_blocked_streak           False                  False
  AMAT           91.67               36            0.26              0.98        546.20                87.24         0.699          pass              0.815             86.9                           0.488               -1.57             -0.257 downtrend_blocked_streak           False                  False
  MRVL           81.08               37            0.01              0.02        218.58               100.52         0.689          pass              0.577             99.6                           0.675                3.59              0.341                       ok           False                  False
  TMUS           80.00                5            3.13              3.88        175.55                55.59         0.614          pass              0.061              0.0                           0.157              -10.10             -0.481  downtrend_blocked_slope           False                  False
 CMCSA           77.78                9            1.95              0.34         24.78                44.00         0.593          pass              0.095             11.8                           0.162                3.93              0.977                       ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot         event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-08-05T10:15:01.723376-04:00 early_entry_1015 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:10:05.726457-04:00 early_entry_1010 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:05:01.598779-04:00 early_entry_1005 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T10:00:04.700543-04:00 early_entry_1000 early_entry_shadow                                                                                                                                                                                                                                                                                                                                                              {"reason": "no_candidate", "shadow_only": true, "would_enter": false}
2026-08-05T00:00:04.689271-04:00     data_refresh       data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 93}
2026-08-04T15:10:06.388254-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:05:01.446900-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T15:00:05.343102-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:55:02.363501-04:00       entry_1500       slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "already_processed"}
2026-08-04T14:50:05.317970-04:00       entry_1500              entry {"allocated_cash": 16400.0, "asset_type": "option", "contract_symbol": "PEP260918C00140000", "contracts": 40, "early_entry_score": 0.423, "entry_mode": "regular", "entry_option_price": 4.1, "execution_mode": "option", "matched_signals": 24, "option_liquidity_status": "ok", "option_open_interest": 3513.0, "option_spread_pct": 4.88, "option_volume": 30.0, "success_rate": 83.33, "ticker": "PEP", "timing_score": 0.544}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.5 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260805101501)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.5 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260805101501)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.5 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260805101501)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.5 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260805101501)

</details>
