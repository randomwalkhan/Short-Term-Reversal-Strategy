# Reversal 3.4.2 Live Paper Test

Latest checkpoint (ET): `2026-05-13 10:55:05 EDT`
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
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- Trend-health gate: block candidates in a short-term down channel when 10d return <= `-1.5%` and either log-slope <= `-0.25%/day` below the 10d lookback average or lower-close streak >= `4`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries use the current option mark price; regular-session stop-loss exits book the planned stop level, with no intraday future path otherwise assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$20,193.50`
- Equity: `$33,663.50`
- Realized PnL: `$23,603.50`
- Unrealized PnL: `$60.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  SNPS     option         option SNPS260618C00490000       2026-05-13                   0      3     13410.0                 13470.0         44.7           44.9      510.62        507.19            60.0                   0.45         97.14               35               0.5         52.16           56.51                  43.23                 154.0           10.0               0.12                      ok
```

## Today's Closed Trades (2026-05-13)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  TEAM           84.21               19            4.21              2.51         83.93               115.69         0.604          pass              0.309             25.4                           0.243               15.51              1.356                                 ok            True                  False
  MDLZ           82.35               17            1.14              0.49         61.49                23.07         0.532          pass              0.211             16.1                           0.151               -0.07              0.018                                 ok            True                  False
  SNPS           96.97               33            1.17              4.21        511.40                43.23         0.531          pass              0.702             32.0                           0.333                5.40              0.683                                 ok            True                  False
    ZS           83.33               36            0.93              0.96        145.76                59.81         0.518          pass              0.484             56.5                           0.379                7.48              1.100                                 ok            True                  False
  FAST           96.43               28            0.55              0.17         43.25                22.09         0.517          pass              0.647             25.0                           0.173               -1.44             -0.327                                 ok            True                  False
   XEL           88.89               27            0.63              0.35         79.75                27.12         0.507          pass              0.583             60.6                           0.619                0.74             -0.221                                 ok            True                  False
  REGN           92.86               28            1.19              6.04        720.82                32.61         0.500          pass              0.607             31.5                           0.176                4.14              0.335                                 ok            True                  False
  CHTR           81.82               22            2.12              2.20        146.98               118.13         0.783          pass              0.338             43.6                           0.755               -8.74             -1.334            downtrend_blocked_slope           False                  False
  GEHC           60.00               25            1.44              0.63         62.02                57.10         0.573          pass              0.246             29.7                           0.262                3.20              0.335                                 ok           False                  False
  ORLY           87.50                8            2.29              1.47         91.21                35.45         0.570          pass              0.287              9.9                           0.183               -2.13             -0.564 downtrend_blocked_slope_and_streak           False                  False
  SHOP           78.95               19            2.96              2.07         98.95                84.62         0.555          pass              0.204             29.4                           0.253              -20.11             -2.549 downtrend_blocked_slope_and_streak           False                  False
   ADP          100.00                9            2.70              4.04        212.08                33.54         0.536          pass              0.550             32.2                           0.215               -3.26             -0.122                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot              event_type                                                                                                                                                                                                                                                                                                                                                                                                                             detail
2026-05-13T10:55:05.050603-04:00 early_entry_1055           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:50:03.713971-04:00 early_entry_1050           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:45:06.364119-04:00 early_entry_1045           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:40:01.859562-04:00 early_entry_1040           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:35:05.886514-04:00 early_entry_1035           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:30:03.887456-04:00 early_entry_1030           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                    {"reason": "daily_entry_limit"}
2026-05-13T10:25:06.096694-04:00 early_entry_1025                   entry {"allocated_cash": 13410.0, "asset_type": "option", "contract_symbol": "SNPS260618C00490000", "contracts": 3, "early_entry_score": 0.822, "entry_mode": "early", "entry_option_price": 44.7, "execution_mode": "option", "matched_signals": 35, "option_liquidity_status": "ok", "option_open_interest": 154.0, "option_spread_pct": 12.08, "option_volume": 10.0, "success_rate": 97.14, "ticker": "SNPS", "timing_score": 0.556}
2026-05-13T10:20:06.278508-04:00 early_entry_1020           entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                         {"reason": "no_candidate"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015           entry_skipped                                                                                                                                                                                                                                                                                                                                                                             {"reason": "no_trade_after_option_and_timing_filters"}
2026-05-13T10:15:05.895485-04:00 early_entry_1015 entry_candidate_skipped                                                                                                                                                            {"early_entry_score": 0.815, "option_liquidity_status": "low_open_interest,low_volume,wide_spread", "option_open_interest": 14.0, "option_spread_pct": 21.38, "option_volume": 8.0, "reason": "no_trade_low_option_liquidity", "ticker": "TTWO", "timing_score": 0.437}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.2 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260513105505)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.2 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260513105505)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.2 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260513105505)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.2 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260513105505)

</details>
