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
1. `AKUN-001-877774-VLESS-WS-102MS` (url=245ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-103MS` (url=215ms, nekobox=237ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-96MS` (url=207ms, nekobox=240ms, status=yes)
4. `AKUN-004-SPEEDTEST-VLESS-WS-96MS` (url=227ms, nekobox=219ms, status=no)
5. `AKUN-004-CLOUDFLARE-VLESS-WS-116MS`
6. `AKUN-006-SPEEDTEST-VLESS-WS-123MS` (url=211ms, nekobox=201ms, status=no)
7. `AKUN-005-AIMALL-VLESS-WS-132MS`
8. `AKUN-006-CLOUDFLARE-VLESS-WS-109MS`
9. `AKUN-007-CHATGPT-VLESS-WS-118MS`
10. `AKUN-008-UNKNOWN-VLESS-WS-94MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-114MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-136MS`
13. `AKUN-013-SPEEDTEST-VLESS-WS-116MS` (url=210ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-176MS` (url=238ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-105MS` (url=445ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-304MS` (url=618ms, status=HTTP 204)
17. `AKUN-018-TW-CLOUD-VLESS-WS-418MS` (url=949ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-116MS` (url=213ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-642MS` (url=1100ms, status=HTTP 204)
20. `AKUN-025-CLOUDFLARE-VLESS-WS-634MS` (url=1025ms, status=HTTP 204)
21. `AKUN-027-CLOUDFLARE-VLESS-WS-708MS` (url=3424ms, status=HTTP 204)
22. `AKUN-028-CLOUDFLARE-VLESS-WS-740MS` (url=1190ms, status=HTTP 204)
23. `AKUN-030-CLOUDFLARE-VLESS-WS-707MS` (url=1159ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-294MS` (url=1231ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-776MS` (url=1224ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
