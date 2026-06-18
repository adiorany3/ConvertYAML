# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 18
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 24

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDWEBMANAGE-EU-FR-VLESS-WS-76MS` (url=198ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=206ms, nekobox=175ms, status=no)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=196ms, nekobox=184ms, status=no)
4. `AKUN-002-008500-VLESS-WS-90MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-100MS`
6. `AKUN-004-CLOUDFLARE-VLESS-WS-97MS`
7. `AKUN-005-UNKNOWN-VLESS-WS-101MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-182MS` (url=297ms, nekobox=281ms, status=no)
10. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-391MS`
13. `AKUN-010-WPENG-VLESS-WS-391MS`
14. `AKUN-015-CLOUDFLARE-VLESS-WS-400MS` (url=864ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-389MS` (url=831ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-448MS` (url=837ms, status=HTTP 204)
17. `AKUN-020-CONFLU-VLESS-WS-386MS` (url=746ms, status=HTTP 204)
18. `AKUN-034-CLOUDFLARE-VLESS-WS-829MS` (url=2243ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
