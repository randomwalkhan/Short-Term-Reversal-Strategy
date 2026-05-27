# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-27 10:45:02 EDT`
Last processed slot: `early_entry_1045`

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

- Cash: `$19,575.25`
- Equity: `$31,695.25`
- Realized PnL: `$21,585.25`
- Unrealized PnL: `$110.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00500000       2026-05-27                   0      2     12010.0                 12120.0        60.05           60.6       531.8        529.76          bid_ask_mid                       60.6                bid_ask_mid                    True           110.0                   0.92         97.22               36              0.52         54.56           57.04                  24.18                 302.0          157.0                0.1                      ok
```

## Today's Closed Trades (2026-05-27)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           87.50               32            0.92              2.14        331.75                92.16         0.641            pass              0.556             48.5                           0.423               12.02              1.215                                 ok            True                  False
  INTC           94.74               19            3.47              3.00        122.24                91.80         0.581            pass              0.612             33.7                           0.376               -1.14              0.377                                 ok            True                  False
  ISRG           85.71               14            2.20              6.72        433.76                35.34         0.521            pass              0.271             13.4                           0.270               -1.12              0.146                                 ok            True                  False
  ASML           92.00               25            2.14             24.41       1621.57                54.27         0.513            pass              0.558             28.9                           0.319                5.01              0.571                                 ok            True                  False
  INSM           72.97               37            1.04              0.79        108.53               110.60         0.735            pass              0.360             35.4                           0.236               -7.12             -0.846            downtrend_blocked_slope           False                  False
   AEP           66.67               12            0.75              0.69        130.61                25.21         0.604            pass              0.178             34.7                           0.266               -1.53              0.148                                 ok           False                  False
  FTNT          100.00                6            4.11              3.85        132.31                66.88         0.583            pass              0.551             30.8                           0.346               12.81              1.397                                 ok           False                  False
  REGN           88.24               34            0.68              3.03        633.32                48.91         0.569            pass              0.601             54.9                           0.338              -12.74             -1.486 downtrend_blocked_slope_and_streak           False                  False
  UPRO           94.59               37            0.09              0.09        145.82                30.88         0.516            pass              0.868             82.4                           0.507                4.44              0.295                                 ok           False                  False
  NVDA           75.00               12            2.50              3.76        213.25                40.94         0.506            pass              0.073              2.9                           0.085               -5.11             -0.709 downtrend_blocked_slope_and_streak           False                  False
  ROST           95.45               44            0.12              0.20        234.60                38.50         0.488 below_threshold              0.927             92.6                           0.696                7.69              1.039                                 ok           False                  False
  LRCX           80.77               26            1.69              3.81        321.05                57.65         0.482 below_threshold              0.281             35.2                           0.322                9.68              0.950                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-27T10:45:02.652833-04:00 early_entry_1045 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:40:01.617422-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-27T10:35:01.630649-04:00 early_entry_1035         entry {"allocated_cash": 12010.0, "asset_type": "option", "contract_symbol": "SNPS260717C00500000", "contracts": 2, "early_entry_score": 0.805, "entry_mode": "early", "entry_option_price": 60.05, "execution_mode": "option", "matched_signals": 36, "option_liquidity_status": "ok", "option_open_interest": 302.0, "option_spread_pct": 9.83, "option_volume": 157.0, "success_rate": 97.22, "ticker": "SNPS", "timing_score": 0.413}
2026-05-27T10:30:06.423656-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:25:01.625508-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:20:05.595233-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:15:02.626707-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:10:01.607453-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:05:01.657651-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-27T10:00:05.617204-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260527104502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260527104502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260527104502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260527104502)

</details>
