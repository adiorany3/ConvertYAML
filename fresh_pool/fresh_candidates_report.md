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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=201ms, nekobox=228ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-59MS` (url=201ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-73MS` (url=199ms, nekobox=235ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-67MS` (url=205ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=200ms, nekobox=223ms, status=yes)
6. `AKUN-006-SPEEDTEST-VLESS-WS-62MS` (url=212ms, nekobox=171ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-73MS`
8. `AKUN-007-CHATGPT-VLESS-WS-66MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-75MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-62MS` (url=200ms, status=HTTP 204)
13. `AKUN-014-SPEEDTEST-VLESS-WS-88MS` (url=215ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-93MS` (url=201ms, status=HTTP 204)
15. `AKUN-016-LEVIKOGJGFDD-VLESS-WS-100MS` (url=201ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-66MS` (url=207ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-80MS` (url=204ms, status=HTTP 204)
18. `AKUN-019-DEV-VLESS-WS-57MS` (url=205ms, status=HTTP 204)
19. `AKUN-020-RMGYVPN-VLESS-WS-119MS` (url=313ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-353MS` (url=761ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-340MS` (url=717ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-387MS` (url=660ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-401MS` (url=735ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-435MS` (url=751ms, status=HTTP 204)
25. `AKUN-031-UNKNOWN-VLESS-WS-420MS` (url=736ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
