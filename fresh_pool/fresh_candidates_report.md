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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-95MS` (url=331ms, nekobox=339ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-113MS` (url=296ms, nekobox=342ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-118MS` (url=306ms, nekobox=311ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-123MS` (url=287ms, nekobox=334ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-116MS` (url=369ms, nekobox=309ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-125MS` (url=282ms, nekobox=224ms, status=no)
7. `AKUN-006-CLOUDFLARE-VLESS-WS-124MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-133MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS` (url=319ms, nekobox=337ms, status=yes)
10. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-141MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-142MS`
12. `AKUN-012-PUBLICDOMAINREGISTRY-NET-VLESS-WS-127MS` (url=363ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-151MS` (url=279ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-151MS` (url=320ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-142MS` (url=270ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-166MS` (url=330ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-132MS` (url=323ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-151MS` (url=327ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-120MS` (url=292ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-133MS` (url=300ms, status=HTTP 204)
21. `AKUN-021-VOV-VLESS-WS-139MS` (url=359ms, status=HTTP 204)
22. `AKUN-022-WPENG-VLESS-WS-110MS` (url=328ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-180MS` (url=343ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-127MS` (url=342ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-315MS` (url=671ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
