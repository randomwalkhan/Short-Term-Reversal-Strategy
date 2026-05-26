# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:20:01 EDT`
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

- Cash: `$2,162.75`
- Equity: `$32,162.75`
- Realized PnL: `$20,637.75`
- Unrealized PnL: `$1,525.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260717C00230000       2026-05-26                   0     15     14700.0                 15750.0         9.80          10.50      225.59        224.77          bid_ask_mid                      10.50                bid_ask_mid                    True          1050.0                   7.14        100.00               35              0.86         35.64           40.83                  35.40                 169.0           22.0               0.12                      ok
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14250.0         3.62           3.75      103.16        101.22          bid_ask_mid                       3.75                bid_ask_mid                    True           475.0                   3.45         94.74               19              0.93         28.13           38.99                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26        30.35       36.15 2320.0   19.110379 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
   TRI           80.00               20            0.69              0.42         85.68                55.00         0.639          pass              0.353             74.1                           0.830               -3.71              0.135                      ok            True                  False
  FTNT          100.00               33            1.05              0.98        133.51                66.43         0.613          pass              0.829             71.5                           0.608               14.80              1.630                      ok            True                   True
  MELI           92.00               25            1.91             22.24       1654.89                60.80         0.568          pass              0.578             33.8                           0.480                4.84              0.679                      ok            True                  False
  PAYX           90.91               11            1.34              0.91         96.61                28.52         0.549          pass              0.518             55.3                           0.717                3.25              0.595                      ok            True                  False
  ROST           90.91               22            1.11              1.82        234.03                38.50         0.549          pass              0.512             28.8                           0.231                8.23              0.742                      ok            True                  False
   ADP           94.12               17            1.86              2.94        224.05                37.70         0.538          pass              0.555             25.9                           0.489                4.46              0.664                      ok            True                  False
  CTSH           88.46               26            1.19              0.44         52.56                46.65         0.528          pass              0.571             61.8                           0.744                6.57              1.336                      ok            True                  False
   ROP           90.48               21            1.36              3.12        325.60                26.18         0.509          pass              0.492             29.5                           0.332               -1.92              0.064                      ok            True                  False
  INTU           86.67               30            1.34              3.00        318.66                90.56         0.684          pass              0.564             61.6                           0.801              -19.74             -2.177 downtrend_blocked_slope           False                  False
  CSCO           80.00                5            2.40              2.02        119.54                52.25         0.631          pass              0.102             13.0                           0.193               19.05              1.859                      ok           False                  False
  SBUX          100.00                8            1.83              1.32        102.54                33.02         0.617          pass              0.493             10.4                           0.185               -3.71             -0.294 downtrend_blocked_slope           False                  False
   AEP           71.43               14            0.59              0.54        131.36                25.20         0.599          pass              0.229             47.6                           0.273                0.09              0.060                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-26T10:20:01.300698-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:15:02.302661-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:10:01.332535-04:00 early_entry_1010                   entry {"allocated_cash": 14700.0, "asset_type": "option", "contract_symbol": "TTWO260717C00230000", "contracts": 15, "early_entry_score": 0.809, "entry_mode": "early", "entry_option_price": 9.8, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.24, "option_volume": 22.0, "success_rate": 100.0, "ticker": "TTWO", "timing_score": 0.397}
2026-05-26T10:10:01.332535-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.848, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 53.06, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-26T10:05:02.315056-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-26T10:05:02.315056-04:00 early_entry_1005 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.842, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 50.98, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.611}
2026-05-26T10:05:02.315056-04:00      manage_1000                    exit                                                                                                                                                                                                                                            {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 36.15, "pnl": 2320.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 19.11, "ticker": "AVGO"}
2026-05-26T10:00:03.313012-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                   {"reason": "max_open_positions"}
2026-05-26T00:00:03.086607-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                      {'saved': 92}
2026-05-25T23:55:01.101287-04:00   share_ext_2355           market_closed                                                                                                                                                                                                                                                                                                                                                                         {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526102001)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526102001)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526102001)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526102001)

</details>
