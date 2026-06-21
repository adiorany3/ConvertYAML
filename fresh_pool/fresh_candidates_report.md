# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-95MS` (url=313ms, nekobox=271ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-96MS` (url=231ms, nekobox=247ms, status=yes)
3. `AKUN-003-VULTR-VLESS-WS-109MS` (url=206ms, nekobox=265ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-112MS` (url=228ms, nekobox=246ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-100MS` (url=231ms, nekobox=313ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-111MS` (url=272ms, nekobox=267ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-115MS` (url=221ms, nekobox=233ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-118MS` (url=230ms, nekobox=260ms, status=yes)
9. `AKUN-009-SPEEDTEST-VLESS-WS-123MS` (url=260ms, nekobox=313ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-115MS` (url=267ms, nekobox=281ms, status=yes)
11. `AKUN-011-GO-DADDY-COM-LLC-VLESS-WS-131MS` (url=238ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-137MS` (url=289ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-127MS` (url=237ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-138MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-366MS` (url=746ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-387MS` (url=757ms, status=HTTP 204)
17. `AKUN-017-MICROSOFT-VLESS-WS-416MS` (url=863ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-408MS` (url=857ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-413MS` (url=815ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-422MS` (url=873ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-420MS` (url=758ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-675MS` (url=1035ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-786MS` (url=1456ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-894MS` (url=1370ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
