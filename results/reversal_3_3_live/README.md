# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-28 10:30:05 EDT`
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

- Cash: `$17,884.25`
- Equity: `$31,304.25`
- Realized PnL: `$20,384.25`
- Unrealized PnL: `$920.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  AVGO     option         option AVGO260717C00420000       2026-05-28                   0      4     12500.0                 13420.0        31.25          33.55      419.65        418.67          bid_ask_mid                      33.55                bid_ask_mid                    True           920.0                   7.36         89.19               37              0.52         51.04            54.6                  36.99                2631.0           27.0               0.06                      ok
```

## Today's Closed Trades (2026-05-28)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price     pnl  return_pct           exit_reason
  SNPS     option         option SNPS260717C00500000      2          2026-05-27         2026-05-28        60.05      54.045 -1201.0       -10.0 stop_loss_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  CSCO           92.31               26            0.86              0.72        119.36                51.65         0.617          pass              0.616             39.8                           0.420               16.46              0.869                      ok            True                  False
  ROST           90.00               10            1.79              2.93        232.21                38.54         0.600          pass              0.425             32.6                           0.495                8.27              1.171                      ok            True                  False
   XEL           95.45               22            1.00              0.57         80.76                25.49         0.544          pass              0.538              1.2                           0.191                0.35              0.231                      ok            True                  False
  INTC           95.00               20            3.42              2.92        120.52                92.16         0.543          pass              0.594             24.2                           0.289               -2.24              0.670                      ok            True                  False
  LRCX           86.21               29            1.09              2.43        317.89                56.04         0.536          pass              0.544             66.0                           0.828                6.78              1.134                      ok            True                  False
   LIN           83.33               12            1.60              5.69        505.43                20.85         0.513          pass              0.190             12.3                           0.183               -2.63             -0.062                      ok            True                  False
  MNST           91.67               36            0.54              0.34         89.10                49.17         0.507          pass              0.719             61.3                           0.611                3.29              0.263                      ok            True                   True
    ZS           85.19               27            1.72              1.52        125.76               152.21         0.828          pass              0.475             46.9                           0.617              -18.49             -1.212 downtrend_blocked_slope           False                  False
  SOXL           90.62               32            0.27              0.40        217.81               139.87         0.727          pass              0.796             97.8                           0.925               18.00              2.755                      ok           False                  False
  MELI           95.00               40            0.30              3.58       1694.64                61.41         0.614          pass              0.860             66.3                           0.444                8.26              0.863                      ok           False                  False
  AMAT           88.89               36            0.15              0.46        448.05                50.47         0.562          pass              0.747             93.4                           0.939                2.64              0.429                      ok           False                  False
   AEP           75.00               12            1.08              0.98        129.15                25.33         0.559          pass              0.248             59.7                           0.313                0.17              0.217                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                              detail
2026-05-28T10:30:05.932623-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:25:06.392243-04:00 early_entry_1025 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:20:03.857163-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:15:02.929662-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:10:02.928305-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "daily_entry_limit"}
2026-05-28T10:05:05.949315-04:00 early_entry_1005         entry {"allocated_cash": 12500.0, "asset_type": "option", "contract_symbol": "AVGO260717C00420000", "contracts": 4, "early_entry_score": 0.738, "entry_mode": "early", "entry_option_price": 31.25, "execution_mode": "option", "matched_signals": 37, "option_liquidity_status": "ok", "option_open_interest": 2631.0, "option_spread_pct": 5.76, "option_volume": 27.0, "success_rate": 89.19, "ticker": "AVGO", "timing_score": 0.427}
2026-05-28T10:05:05.949315-04:00      manage_1000          exit                                                                                                                                                                                                                                                  {"asset_type": "option", "contract_symbol": "SNPS260717C00500000", "fill_price": 54.045, "pnl": -1201.0, "reason": "stop_loss_hit_at_scan", "return_pct": -10.0, "ticker": "SNPS"}
2026-05-28T10:00:04.925583-04:00 early_entry_1000 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                          {"reason": "no_candidate"}
2026-05-28T00:00:03.757313-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                       {'saved': 92}
2026-05-27T15:10:02.000661-04:00       entry_1500  slot_skipped                                                                                                                                                                                                                                                                                                                                                                                                     {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260528103005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260528103005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260528103005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260528103005)

</details>
