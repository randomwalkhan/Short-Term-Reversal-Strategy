# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-06-01 10:40:02 EDT`
Last processed slot: `manage_1030`

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

- Cash: `$16,749.25`
- Equity: `$32,049.25`
- Realized PnL: `$20,849.25`
- Unrealized PnL: `$1,200.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260717C00470000       2026-05-29                   1      4     14100.0                 15300.0        35.25          38.25      477.34        477.71          bid_ask_mid                      38.25                bid_ask_mid                    True          1200.0                   8.51         97.22               36              0.69         45.69            50.9                  40.06                 115.0           67.0               0.11                      ok
```

## Today's Closed Trades (2026-06-01)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  MRVL     option         option MRVL260717C00200000      5          2026-06-01         2026-06-01         28.3       25.47 -1415.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day trend_health_status  call_candidate  early_entry_candidate
  SOXL           92.86               28            1.14              1.78        223.58               138.67         0.745          pass              0.784             82.0                           0.907               35.09              4.488                  ok            True                  False
  ROST           93.75               16            1.45              2.34        230.73                40.27         0.593          pass              0.576             36.7                           0.458                7.35              1.039                  ok            True                  False
  LRCX           88.46               26            1.49              3.31        316.76                55.15         0.544          pass              0.560             57.7                           0.634               10.09              1.560                  ok            True                  False
  KLAC           88.46               26            1.28             17.16       1914.36                50.27         0.539          pass              0.480             31.4                           0.283                5.28              1.042                  ok            True                  False
  AAPL           92.31               13            1.43              3.13        310.72                17.18         0.533          pass              0.404              1.0                           0.164                2.45              0.461                  ok            True                  False
  MDLZ           92.31               13            1.34              0.57         60.92                14.75         0.517          pass              0.417              5.7                           0.113               -0.15              0.022                  ok            True                  False
  ISRG           80.00               15            2.14              6.37        421.91                37.20         0.510          pass              0.172             29.1                           0.174               -1.33             -0.437                  ok            True                  False
  FAST           92.86               14            1.52              0.47         44.00                16.05         0.501          pass              0.420              0.0                           0.040                0.62              0.184                  ok            True                  False
  INSM           68.00               25            2.34              1.75        106.16               110.85         0.732          pass              0.208             11.7                           0.158               -4.33             -0.216                  ok           False                  False
  MELI           95.00               40            0.36              4.32       1693.80                60.97         0.597          pass              0.831             57.2                           0.333                9.22              0.844                  ok           False                  False
  ASML           94.12               34            0.46              5.19       1610.53                52.38         0.585          pass              0.818             74.2                           0.727                6.89              0.972                  ok           False                  False
   AEP           57.14                7            1.33              1.18        126.17                24.34         0.560          pass              0.109             17.6                           0.281               -0.13             -0.040                  ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                            detail
2026-06-01T10:40:02.889007-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:35:01.685578-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:30:02.004330-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:25:05.840855-04:00      manage_1030          exit                                                                                                                                                                                                                                                 {"asset_type": "option", "contract_symbol": "MRVL260717C00200000", "fill_price": 25.47, "pnl": -1415.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "MRVL"}
2026-06-01T10:20:03.923727-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "daily_entry_limit"}
2026-06-01T10:15:04.991229-04:00 early_entry_1015         entry {"allocated_cash": 14150.0, "asset_type": "option", "contract_symbol": "MRVL260717C00200000", "contracts": 5, "early_entry_score": 0.862, "entry_mode": "early", "entry_option_price": 28.3, "execution_mode": "option", "matched_signals": 32, "option_liquidity_status": "ok", "option_open_interest": 4958.0, "option_spread_pct": 5.3, "option_volume": 50.0, "success_rate": 100.0, "ticker": "MRVL", "timing_score": 0.526}
2026-06-01T10:10:06.342773-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:05:05.997517-04:00 early_entry_1005 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                        {"reason": "no_candidate"}
2026-06-01T10:00:03.895970-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                            {"reason": "no_trade_after_option_and_timing_filters"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260601104002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260601104002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260601104002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260601104002)

</details>
