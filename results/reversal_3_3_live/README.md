# Reversal 3.3 Live Paper Test

Latest checkpoint (ET): `2026-04-29 10:10:03 EDT`
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
- Exit scans: `9:30 AM ET` and every `30` minutes through `4:00 PM ET`; off-hours `5-minute` checkpoints continue mark-to-market updates for open positions, while any legacy share positions still held from older versions continue extended-hours take-profit and stop loss scans until flat
- Live exit ladder: `+15% / +15% / -12%`
- Option entry liquidity gate: `open interest >= 100`, `volume >= 10`, `spread <= 15%`
- Entry timing overlay: short-window technical-indicator score using a `5d` feature window; only trade when `timing_score >= 0.50`
- No-trade rule: if the option is unavailable or fails the liquidity gate, skip the signal rather than falling back into shares
- Extended-hours handling: open option positions continue to refresh their paper marks on off-hours checkpoints; legacy share positions, if any, can still trigger take-profit fills at the target price and stop loss exits at the current visible quote
- Practical live-paper adjustment: entries and exits use the current option mark price; no intraday future path is assumed
- Chart views: `Overall / 1D / 1W / 1M`, default open panel is `Overall`

## Portfolio Snapshot

- Cash: `$7,922.50`
- Equity: `$16,897.50`
- Realized PnL: `$4,997.50`
- Unrealized PnL: `$1,900.00`
- Open positions: `1`

## Open Positions

```text
ticker asset_type execution_mode          instrument entry_trade_date  business_days_held  units  cash_spent  current_position_value  entry_price  current_price  entry_spot  current_spot  unrealized_pnl  unrealized_return_pct  success_rate  matched_signals  current_drop_pct  entry_iv_pct  current_iv_pct  rolling_sigma_20d_pct  option_open_interest  option_volume  option_spread_pct option_liquidity_status
  INTC     option         option INTC260529C00084000       2026-04-28                   1     10      7075.0                  8975.0         7.08           8.98       84.22         88.94          1900.0                  26.86         100.0               38              0.91         70.58           61.16                  91.28                 369.0           78.0               0.05                      ok
```

## Today's Closed Trades (2026-04-29)

_None_

## Current Screener Snapshot

```text
ticker  success_rate_%  matched_signals  current_drop_%  target_rebound_$  target_price  rolling_sigma_20d_%  call_candidate
  CHTR           87.50               24            1.75              2.12        172.11               113.02            True
 CMCSA           93.75               16            0.80              0.15         27.58                60.29            True
  CDNS          100.00               12            2.72              6.21        322.68                53.80            True
  NFLX           87.88               33            0.80              0.51         92.07                46.23            True
  SNPS           95.00               20            2.15              7.28        480.77                50.93            True
  DDOG           90.00               30            1.41              1.30        130.99                52.25            True
  ADSK           87.50               32            0.95              1.55        234.18                45.23            True
  FAST           91.89               37            0.50              0.16         44.61                39.66            True
  TEAM           85.42               48            0.43              0.21         69.62                78.64           False
  CRWD           79.17               24            1.65              5.27        452.73                53.30           False
  ASML           87.80               41            0.03              0.32       1384.42                50.71           False
    ZS           77.27               22            2.72              2.59        134.96                65.17           False
```

## Recent Events

```text
                    timestamp_et         slot   event_type                          detail
2026-04-29T10:10:03.767251-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T10:05:08.240355-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T10:00:04.620825-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T09:55:04.061412-04:00  manage_1000 slot_skipped {"reason": "already_processed"}
2026-04-29T09:40:03.886159-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:35:04.233499-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:30:03.967315-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T09:25:06.961152-04:00  manage_0930 slot_skipped {"reason": "already_processed"}
2026-04-29T00:01:06.010136-04:00 data_refresh data_refresh                   {'saved': 99}
2026-04-28T16:10:03.932296-04:00  manage_1600 slot_skipped {"reason": "already_processed"}
```

## Equity Curves

The `Overall` chart compares Strategy, QQQ, and SPY from the live-paper start date using the same initial capital. The `1D / 1W / 1M` charts focus on strategy-only performance over each trailing window. The latest point is annotated with its exact ET checkpoint time and return %.

<details open>
<summary><strong>Overall</strong></summary>

![Reversal 3.3 Live Equity Overall](../../assets/reversal_3_3_live_equity_overall.png?v=20260429101003)

</details>

<details>
<summary><strong>1D</strong></summary>

![Reversal 3.3 Live Equity 1D](../../assets/reversal_3_3_live_equity_1d.png?v=20260429101003)

</details>

<details>
<summary><strong>1W</strong></summary>

![Reversal 3.3 Live Equity 1W](../../assets/reversal_3_3_live_equity.png?v=20260429101003)

</details>

<details>
<summary><strong>1M</strong></summary>

![Reversal 3.3 Live Equity 1M](../../assets/reversal_3_3_live_equity_1m.png?v=20260429101003)

</details>
