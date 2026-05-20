# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-20 10:50:01 EDT`
Last processed slot: `manage_1100`

## Active Configuration

- Universe: `qqq_plus_leverage_etfs` (`qqq_only_filtered + SOXL + UPRO`)
- Lookback window: `60d`
- Minimum current drop: `> 0.5%`
- Recovery target: `70% of the signal-day drop`
- Success-rate gate: `>= 80%`
- Matched-signal gate: `>= 10`
- Positioning: `50%` target allocation per new entry, up to `2` concurrent tickers
- Entry scan: `3:00 PM ET`
- Early-entry permission: `10:00 AM-12:00 PM ET` 5-minute scans may enter one exceptional candidate only when `early_entry_score >= 0.67`, success rate `>= 88%`, matched signals `>= 30`, early reclaim `>= 60%`, and recovery stability `>= 0.55`; the one-new-entry-per-day limit still applies
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

- Cash: `$14,107.75`
- Equity: `$26,847.75`
- Realized PnL: `$16,462.75`
- Unrealized PnL: `$385.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  FTNT     option         option FTNT260717C00125000       2026-05-20                   0     14     12355.0                 12740.0         8.82            9.1      126.75        127.83          bid_ask_mid                        9.1                bid_ask_mid                    True           385.0                   3.12         100.0               38              0.69         41.39           40.33                  70.74                1300.0           40.0               0.12                      ok
```

## Today's Closed Trades (2026-05-20)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
   WMT           92.86               14            1.24              1.17        133.70                20.68         0.525            pass              0.611             63.1                           0.726                2.08              0.339                                 ok            True                  False
 GOOGL           86.21               29            0.87              2.37        386.65                41.27         0.520            pass              0.431             28.9                           0.232               -3.46             -0.213                                 ok            True                  False
  ADSK           86.96               23            1.28              2.19        243.22                38.52         0.503            pass              0.537             71.4                           0.725               -0.85             -0.151                                 ok            True                  False
  AMGN           83.33               24            0.60              1.40        330.15                26.77         0.502            pass              0.470             79.3                           0.492                0.04              0.002                                 ok            True                  False
  TMUS           80.95               21            1.62              2.20        192.48                36.70         0.502            pass              0.173              8.2                           0.083               -1.49             -0.204                                 ok            True                  False
   TXN           93.94               33            0.13              0.28        302.19                69.06         0.642            pass              0.879             96.7                           0.518                4.31              0.591                                 ok           False                  False
  TEAM           88.57               35            1.68              1.02         86.18               114.61         0.619            pass              0.658             67.0                           0.575               -4.10             -0.531 downtrend_blocked_slope_and_streak           False                  False
  FTNT          100.00               48            0.02              0.01        127.63                70.74         0.599            pass              0.957             99.2                           0.845               41.88              2.654                                 ok           False                  False
  PAYX           95.45               22            0.25              0.17         94.41                29.36         0.558            pass              0.812             92.0                           0.827                4.46              0.245                                 ok           False                  False
  CTSH           85.71               21            1.37              0.49         50.67                50.98         0.526            pass              0.472             64.5                           0.706               -1.54             -0.228           downtrend_blocked_streak           False                  False
  GOOG           85.71               28            0.86              2.31        383.91                41.08         0.515            pass              0.421             32.5                           0.251               -3.43             -0.221           downtrend_blocked_streak           False                  False
  SNPS           97.14               35            0.54              1.87        493.07                41.71         0.499 below_threshold              0.877             86.7                           0.874               -2.62             -0.355 downtrend_blocked_slope_and_streak           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                               detail
2026-05-20T10:50:01.057025-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:45:05.974600-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:40:03.515008-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:35:01.049335-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:30:01.058983-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                      {"reason": "daily_entry_limit"}
2026-05-20T10:25:06.944713-04:00 early_entry_1025                   entry {"allocated_cash": 12355.0, "asset_type": "option", "contract_symbol": "FTNT260717C00125000", "contracts": 14, "early_entry_score": 0.837, "entry_mode": "early", "entry_option_price": 8.825, "execution_mode": "option", "matched_signals": 38, "option_liquidity_status": "ok", "option_open_interest": 1300.0, "option_spread_pct": 11.9, "option_volume": 40.0, "success_rate": 100.0, "ticker": "FTNT", "timing_score": 0.622}
2026-05-20T10:21:54.079183-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                               {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                               {"early_entry_score": 0.683, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 1.0, "option_spread_pct": 46.51, "option_volume": 0.0, "reason": "no_trade_low_option_liquidity", "ticker": "CTAS", "timing_score": 0.458}
2026-05-20T10:21:54.079183-04:00 early_entry_1020 entry_candidate_skipped                                                                                                                                                                         {"early_entry_score": 0.801, "option_liquidity_status": "low_open_interest,wide_spread", "option_open_interest": 29.0, "option_spread_pct": 26.59, "option_volume": 20.0, "reason": "no_trade_low_option_liquidity", "ticker": "ADP", "timing_score": 0.484}
2026-05-20T10:05:07.673831-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                           {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260520105001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260520105001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260520105001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260520105001)

</details>
