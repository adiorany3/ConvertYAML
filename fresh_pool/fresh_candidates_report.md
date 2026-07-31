# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=208ms, nekobox=239ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=217ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=253ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, nekobox=172ms, status=no)
5. `AKUN-004-UNKNOWN-VLESS-WS-61MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-58MS` (url=225ms, nekobox=171ms, status=no)
7. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-55MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-64MS` (url=226ms, nekobox=183ms, status=no)
10. `AKUN-007-UNKNOWN-VLESS-WS-98MS`
11. `AKUN-008-UNKNOWN-VLESS-WS-171MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-62MS` (url=226ms, nekobox=171ms, status=no)
13. `AKUN-009-090227-VLESS-WS-270MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-448MS`
15. `AKUN-017-UNKNOWN-VLESS-WS-517MS` (url=648ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-59MS` (url=221ms, status=HTTP 204)
17. `AKUN-019-NET-141-11-202-0-23-VLESS-WS-385MS` (url=728ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-612MS` (url=729ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-571MS` (url=1725ms, status=HTTP 204)
20. `AKUN-023-GAMEFICTOINSPEED-VLESS-WS-703MS` (url=1032ms, status=HTTP 204)
21. `AKUN-024-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-686MS` (url=2581ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-735MS` (url=1252ms, status=HTTP 204)
23. `AKUN-027-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-744MS` (url=1659ms, status=HTTP 204)
24. `AKUN-028-PLAY2GO-CUSTOMERS-NETWOR-VLESS-WS-718MS` (url=1812ms, status=HTTP 204)
25. `AKUN-029-CLOUDFLARE-VLESS-WS-122MS` (url=222ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
