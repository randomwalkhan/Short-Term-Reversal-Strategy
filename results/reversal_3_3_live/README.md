# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:05:02 EDT`
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

- Cash: `$16,862.75`
- Equity: `$31,017.75`
- Realized PnL: `$20,637.75`
- Unrealized PnL: `$380.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 14155.0         3.62           3.72      103.16        102.44          bid_ask_mid                       3.72                bid_ask_mid                    True           380.0                   2.76         94.74               19              0.93         28.13           35.32                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26        30.35       36.15 2320.0   19.110379 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  FTNT          100.00               34            0.97              0.91        133.54                66.43         0.611          pass              0.842             73.7                           0.762               14.90              1.634                      ok            True                   True
  SBUX           95.65               23            0.64              0.47        102.91                33.02         0.595          pass              0.666             40.0                           0.256               -2.55             -0.239                      ok            True                  False
  ASML           88.24               34            0.65              7.44       1629.71                54.77         0.579          pass              0.547             36.4                           0.211                3.61              0.371                      ok            True                  False
  MELI           92.00               25            1.83             21.32       1655.28                60.80         0.573          pass              0.587             36.5                           0.567                4.92              0.682                      ok            True                  False
   PEP           90.91               11            1.62              1.71        149.84                20.74         0.541          pass              0.424             24.0                           0.255               -0.86             -0.062                      ok            True                  False
   ADP           89.47               19            1.69              2.66        224.17                37.70         0.529          pass              0.464             32.9                           0.461                4.65              0.672                      ok            True                  False
  CTSH           89.66               29            0.99              0.36         52.59                46.65         0.523          pass              0.642             68.5                           0.756                6.80              1.345                      ok            True                  False
  ROST           93.55               31            0.79              1.30        234.25                38.50         0.509          pass              0.699             49.0                           0.406                8.58              0.757                      ok            True                  False
  TEAM           91.30               46            0.06              0.04         85.40               109.49         0.694          pass              0.866             98.4                           0.909               -2.23              0.076                      ok           False                  False
  INTU           82.61               23            2.01              4.51        318.01                90.56         0.681          pass              0.351             42.2                           0.557              -20.29             -2.208 downtrend_blocked_slope           False                  False
   TRI           75.00               16            1.15              0.69         85.56                55.00         0.630          pass              0.275             57.2                           0.514               -4.15              0.114                      ok           False                  False
  CSCO           80.00                5            2.45              2.07        119.52                52.25         0.630          pass              0.079              5.3                           0.127               18.98              1.856                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                 detail
2026-05-26T10:05:02.315056-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                 {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-26T10:05:02.315056-04:00 early_entry_1005 entry_candidate_skipped {"early_entry_score": 0.842, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 50.98, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.611}
2026-05-26T10:05:02.315056-04:00      manage_1000                    exit                                                                                {"asset_type": "option", "contract_symbol": "AVGO260717C00420000", "fill_price": 36.15, "pnl": 2320.0, "reason": "take_profit_day2_hit_at_scan", "return_pct": 19.11, "ticker": "AVGO"}
2026-05-26T10:00:03.313012-04:00 early_entry_1000           entry_skipped                                                                                                                                                                                                                                       {"reason": "max_open_positions"}
2026-05-26T00:00:03.086607-04:00     data_refresh            data_refresh                                                                                                                                                                                                                                                          {'saved': 92}
2026-05-25T23:55:01.101287-04:00   share_ext_2355           market_closed                                                                                                                                                                                                             {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:50:02.099383-04:00   share_ext_2350           market_closed                                                                                                                                                                                                             {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:45:01.097228-04:00   share_ext_2345           market_closed                                                                                                                                                                                                             {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:40:05.102217-04:00   share_ext_2340           market_closed                                                                                                                                                                                                             {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
2026-05-25T23:35:01.093781-04:00   share_ext_2335           market_closed                                                                                                                                                                                                             {"holiday_name": "Memorial Day", "reason": "nyse_holiday"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526100502)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526100502)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526100502)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526100502)

</details>
