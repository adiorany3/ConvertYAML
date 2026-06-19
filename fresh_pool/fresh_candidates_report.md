# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-62MS` (url=232ms, nekobox=255ms, status=yes)
2. `AKUN-002-AMAZON-VLESS-WS-60MS` (url=230ms, nekobox=231ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-72MS` (url=203ms, nekobox=266ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=241ms, nekobox=260ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=233ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=213ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-75MS` (url=212ms, nekobox=177ms, status=no)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS` (url=239ms, nekobox=179ms, status=no)
9. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS`
10. `AKUN-008-CLOUDWEBMANAGE-EU-FR-VLESS-WS-95MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-76MS`
12. `AKUN-010-US-VLESS-WS-77MS`
13. `AKUN-013-1PASSWORD-VLESS-WS-83MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-167MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-ADF-VLESS-WS-94MS` (url=229ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-355MS` (url=788ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-352MS` (url=748ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-393MS` (url=837ms, status=HTTP 204)
19. `AKUN-019-SPEEDTEST-VLESS-WS-406MS` (url=2560ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-393MS` (url=836ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-418MS` (url=816ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-388MS` (url=805ms, status=HTTP 204)
23. `AKUN-023-JISON-VLESS-WS-537MS` (url=896ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
