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
- Proxy di openclash_fresh_pool.yaml: 31

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
1. `AKUN-001-104-253-175-0-1-VLESS-WS-71MS` (url=237ms, nekobox=259ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS` (url=240ms, nekobox=264ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=235ms, nekobox=295ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=230ms, nekobox=325ms, status=yes)
5. `AKUN-005-154-83-95-0-154-83-95-25-VLESS-WS-94MS` (url=236ms, nekobox=264ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-86MS` (url=232ms, nekobox=274ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-93MS` (url=280ms, nekobox=182ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-103MS`
9. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-106MS`
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-302MS`
11. `AKUN-012-UNKNOWN-VLESS-WS-316MS` (url=4673ms, nekobox=397ms, status=no)
12. `AKUN-010-CLOUDFLARE-VLESS-WS-330MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-295MS` (url=620ms, status=HTTP 204)
14. `AKUN-016-NET-88-216-66-0-23-VLESS-WS-450MS` (url=773ms, status=HTTP 204)
15. `AKUN-018-NET-88-216-66-0-23-VLESS-WS-456MS` (url=765ms, status=HTTP 204)
16. `AKUN-020-GSMVPTUN-VLESS-WS-484MS` (url=788ms, status=HTTP 204)
17. `AKUN-021-UNKNOWN-VLESS-WS-485MS` (url=832ms, status=HTTP 204)
18. `AKUN-022-UNKNOWN-VLESS-WS-504MS` (url=739ms, status=HTTP 204)
19. `AKUN-023-UNKNOWN-VLESS-WS-477MS` (url=807ms, status=HTTP 204)
20. `AKUN-026-UNKNOWN-VLESS-WS-531MS` (url=858ms, status=HTTP 204)
21. `AKUN-028-GSMVPTUN-VLESS-WS-530MS` (url=1791ms, status=HTTP 204)
22. `AKUN-029-IRATOM-VLESS-WS-549MS` (url=1284ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-594MS` (url=1237ms, status=HTTP 204)
24. `AKUN-031-GSMVPTUN-VLESS-WS-648MS` (url=1156ms, status=HTTP 204)
25. `AKUN-032-GSMVPTUN-VLESS-WS-659MS` (url=1107ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
