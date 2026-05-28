# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 10:10:02 EDT`
Last processed slot: `manage_1000`

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

- Cash: `$17,884.25`
- Equity: `$30,104.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$-280.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 12220.0        31.25          30.55      419.65        419.45          bid_ask_mid                      30.55                bid_ask_mid                    True          -280.0                  -2.24         89.19               37              0.52         51.04            50.2                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score   timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
    MU           85.29               34            0.84              5.46        926.07               100.84         0.667            pass              0.620             83.9                           0.471               14.56              2.104                      ok            True                  False
  CSCO           91.67               24            1.14              0.96        119.26                51.65         0.611            pass              0.525             19.9                           0.216               16.13              0.856                      ok            True                  False
  SOXL           86.96               23            3.21              4.90        215.88               139.87         0.597            pass              0.552             73.5                           0.405               14.51              2.619                      ok            True                  False
  AMAT           85.19               27            1.11              3.48        446.76                50.47         0.554            pass              0.458             50.4                           0.551                1.66              0.385                      ok            True                  False
  INTC           95.24               21            3.32              2.83        120.56                92.16         0.544            pass              0.607             26.5                           0.165               -2.13              0.675                      ok            True                  False
   XEL           90.32               31            0.60              0.34         80.85                25.49         0.505            pass              0.582             38.8                           0.317                0.75              0.250                      ok            True                  False
  MNST           91.67               36            0.59              0.37         89.08                49.17         0.503            pass              0.706             57.3                           0.506                3.24              0.261                      ok            True                  False
  LRCX           83.33               24            2.09              4.68        316.93                56.04         0.500 below_threshold              0.336             34.4                           0.391                5.69              1.088                      ok            True                  False
    ZS           82.35               17            2.79              2.47        125.35               152.21         0.824            pass              0.231             13.0                           0.194              -19.39             -1.262 downtrend_blocked_slope           False                  False
  MELI           95.00               40            0.29              3.48       1694.68                61.41         0.614            pass              0.863             67.2                           0.516                8.27              0.864                      ok           False                  False
  FTNT          100.00               43            0.36              0.32        127.79                70.83         0.605            pass              0.856             65.2                           0.394                8.31              0.894                      ok           False                  False
  ROST           88.89                9            2.02              3.30        232.06                38.54         0.591            pass              0.369             24.3                           0.259                8.03              1.160                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-28T10:10:02.928305-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:05:05.949315-04:00 early_entry_1005         entry {"allocated_cash": 12500.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.738, "entry_mode": "early", "entry_option_price": 31.25, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2631.0, "option_spread_pct": 5.76, "option_volume": 27.0, "success_rate": 89.19, "ticker": "AVGO", "timing_score": 0.427}
2026-05-28T10:05:05.949315-04:00      manage_1000          exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "SNPS260717C00500000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-28T10:00:04.925583-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-28T00:00:03.757313-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T15:05:04.292282-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T15:00:06.354268-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T14:55:06.489057-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
2026-05-27T14:50:01.720844-04:00       entry_1500 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528101002)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528101002)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528101002)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528101002)

</details>
