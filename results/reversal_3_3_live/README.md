# Reversal 3.4.1 Live Paper Test

Latest checkpoint (ET): `2026-05-11 10:50:08 EDT`
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

- Cash: `$35,353.50`
- Equity: `$35,353.50`
- Realized PnL: `$25,353.50`
- Unrealized PnL: `$0.00`
- Open positions: `0`

## Open Positions

_None_

## Today's Closed Trades (2026-05-11)

```text
ticker asset_type execution_mode         instrument  units entry_trade_date_et exit_trade_date_et  entry_price  exit_price    pnl  return_pct                  exit_reason
   CEG     option         option CEG260618C00290000      7          2026-05-11         2026-05-11         23.2        26.8 2520.0   15.517241 take_profit_day1_hit_at_scan
```

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  timing_score timing_status  early_entry_score  early_reclaim_%  early_recovery_stability_score  trend_return_10d_%  trend_slope_%/day                trend_health_status  call_candidate  early_entry_candidate
  NXPI           80.56               36            0.58              1.20        294.24                87.07         0.705          pass              0.421             54.3                           0.428               23.71              1.924                                 ok            True                  False
  GOOG           83.33               18            1.49              4.15        395.27                37.66         0.576          pass              0.287             28.9                           0.313               12.22              1.426                                 ok            True                  False
  TMUS           86.21               29            0.80              1.08        193.17                36.59         0.540          pass              0.476             43.4                           0.369                5.11              0.273                                 ok            True                  False
  MRVL          100.00               30            1.06              1.26        169.59                55.66         0.531          pass              0.817             76.8                           0.726                6.40              0.818                                 ok            True                   True
    ZS           80.00               20            2.52              2.69        150.98                58.64         0.531          pass              0.154             11.3                           0.202               10.57              1.326                                 ok            True                  False
   WMT           87.50               16            1.23              1.12        129.95                19.38         0.525          pass              0.356             21.2                           0.352                1.16              0.155                                 ok            True                  False
  WDAY           81.25               16            3.07              2.75        126.65                62.51         0.513          pass              0.136              3.8                           0.133                5.16              0.622                                 ok            True                  False
  CDNS           97.30               37            0.54              1.37        362.11                44.64         0.504          pass              0.863             77.5                           0.457                7.19              1.093                                 ok            True                  False
  MDLZ           84.62               26            0.60              0.26         61.44                24.76         0.500          pass              0.510             76.7                           0.472                6.55              0.495                                 ok            True                  False
  CHTR           81.25               16            2.33              2.53        153.78               119.48         0.793          pass              0.265             37.3                           0.339              -13.38             -1.203            downtrend_blocked_slope           False                  False
 CMCSA           90.00               20            0.75              0.13         25.34                62.19         0.702          pass              0.471             22.4                           0.201               -8.38             -0.824 downtrend_blocked_slope_and_streak           False                  False
  MSTR           90.00               40            0.41              0.53        187.36                70.10         0.582          pass              0.782             85.6                           0.580               10.42              1.521                                 ok           False                  False
```

## Recent Events

```text
                    timestamp_et             slot    event_type                                                                                                                                                                                                                                                                                                                                                                                                                           detail
2026-05-11T10:50:08.671190-04:00 early_entry_1050 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:43:44.045089-04:00 early_entry_1040 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00 early_entry_1035 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:37:19.097633-04:00      manage_1030          exit                                                                                                                                                                                                                                             {"asset_type": "option", "contract_symbol": "CEG260618C00290000", "fill_price": 26.8, "pnl": 2520.0, "reason": "take_profit_day1_hit_at_scan", "return_pct": 15.52, "ticker": "CEG"}
2026-05-11T10:30:53.059924-04:00 early_entry_1030 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:24:36.025323-04:00 early_entry_1020 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:18:18.755092-04:00 early_entry_1015 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:12:01.604493-04:00 early_entry_1010 entry_skipped                                                                                                                                                                                                                                                                                                                                                                                                  {"reason": "daily_entry_limit"}
2026-05-11T10:05:43.962541-04:00 early_entry_1005         entry {"allocated_cash": 16240.0, "asset_type": "option", "contract_symbol": "CEG260618C00290000", "contracts": 7, "early_entry_score": 0.766, "entry_mode": "early", "entry_option_price": 23.2, "execution_mode": "option", "matched_signals": 39, "option_liquidity_status": "ok", "option_open_interest": 991.0, "option_spread_pct": 14.66, "option_volume": 18.0, "success_rate": 89.74, "ticker": "CEG", "timing_score": 0.357}
2026-05-11T09:18:42.943466-04:00     data_refresh  data_refresh                                                                                                                                                                                                                                                                                                                                                                                                                    {'saved': 92}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.4.1 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260511105008)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.4.1 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260511105008)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.4.1 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260511105008)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.4.1 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260511105008)

</details>
