# Reversal 3.4.4 Live Paper Test

Latest checkpoint (ET): `2026-05-26 10:40:05 EDT`
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
- Equity: `$31,887.75`
- Realized PnL: `$20,637.75`
- Unrealized PnL: `$1,250.00`
- Open positions: `2`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot current_price_source  current_exit_signal_price current_exit_signal_source  current_quote_reliable  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  TTWO     option         option TTWO260717C00230000       2026-05-26                   0     15     14700.0                 16425.0         9.80          10.95      225.59        223.96          bid_ask_mid                      10.95                bid_ask_mid                    True          1725.0                  11.73        100.00               35              0.86         35.64           41.96                  35.40                 169.0           22.0               0.12                      ok
  SBUX     option         option SBUX260717C00105000       2026-05-22                   1     38     13775.0                 13300.0         3.62           3.50      103.16        101.11          bid_ask_mid                       3.50                bid_ask_mid                    True          -475.0                  -3.45         94.74               19              0.93         28.13           34.64                  32.97                2147.0           78.0               0.07                      ok
```

## Today's Closed Trades (2026-05-26)

```text
ticker asset_type execution_mode          instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
  AVGO     option         option AVGO260717C00420000      4          2026-05-21         2026-05-26        30.35       36.15 2320.0   19.110379 take_profit_day2_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day     trend_health_status  call_candidate  early_entry_candidate
  MELI           90.00               20            2.05             23.87       1654.19                60.80         0.591          pass              0.479             28.9                           0.351                4.69              0.672                      ok            True                  False
   ADP          100.00               12            2.22              3.50        223.81                37.70         0.559          pass              0.504             11.7                           0.204                4.08              0.647                      ok            True                  False
  CTSH           82.35               17            1.82              0.67         52.46                46.65         0.542          pass              0.289             41.8                           0.374                5.90              1.307                      ok            True                  False
  AMGN           84.00               25            0.61              1.46        338.68                27.24         0.528          pass              0.300             13.3                           0.146                3.09              0.227                      ok            True                  False
 CMCSA           85.71               14            1.29              0.23         25.11                20.74         0.524          pass              0.291             19.8                           0.167               -0.60              0.013                      ok            True                  False
   ROP           88.24               17            1.69              3.86        325.29                26.18         0.513          pass              0.356             12.8                           0.140               -2.24              0.049                      ok            True                  False
  CHTR           86.21               29            1.39              1.41        144.54                56.19         0.512          pass              0.398             18.2                           0.233               -3.15             -0.133                      ok            True                  False
  ROST           93.55               31            0.79              1.29        234.26                38.50         0.510          pass              0.700             49.3                           0.604                8.58              0.757                      ok            True                  False
  TEAM           91.30               46            0.33              0.20         85.34               109.49         0.679          pass              0.845             91.8                           0.638               -2.49              0.064                      ok           False                  False
  INTU           80.00               20            2.66              5.96        317.39                90.56         0.657          pass              0.203             23.6                           0.236              -20.81             -2.238 downtrend_blocked_slope           False                  False
  CSCO           83.33                6            1.99              1.68        119.69                52.25         0.653          pass              0.237             27.6                           0.446               19.54              1.877                      ok           False                  False
   TRI           78.95               19            0.82              0.49         85.65                55.00         0.636          pass              0.332             69.6                           0.679               -3.83              0.129                      ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-26T10:40:05.315818-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:35:01.414005-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:30:01.317125-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:25:03.305112-04:00 early_entry_1025           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:20:01.300698-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:15:02.302661-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-26T10:10:01.332535-04:00 early_entry_1010                   entry {"allocated_cash": 14700.0, "asset_type": "option", "contract_symbol": "TTWO260717C00230000", "contracts": 15, "early_entry_score": 0.809, "entry_mode": "early", "entry_option_price": 9.8, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 169.0, "option_spread_pct": 12.24, "option_volume": 22.0, "success_rate": 100.0, "ticker": "TTWO", "timing_score": 0.397}
2026-05-26T10:10:01.332535-04:00 early_entry_1010 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.848, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 53.06, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.615}
2026-05-26T10:05:02.315056-04:00 early_entry_1005           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-26T10:05:02.315056-04:00 early_entry_1005 entry_candidate_skipped                                                                                                                                                             {"early_entry_score": 0.842, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 2.0, "option_spread_pct": 50.98, "option_volume": 2.0, "reason": "no_trade_low_option_liquidity", "ticker": "FTNT", "timing_score": 0.611}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.4 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260526104005)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.4 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260526104005)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.4 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260526104005)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.4 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260526104005)

</details>
