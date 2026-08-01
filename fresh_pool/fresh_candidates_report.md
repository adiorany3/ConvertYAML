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
1. `AKUN-001-UNKNOWN-VLESS-WS-54MS` (url=225ms, nekobox=235ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-54MS` (url=230ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-54MS` (url=228ms, nekobox=233ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=196ms, nekobox=173ms, status=no)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-59MS` (url=224ms, nekobox=171ms, status=no)
6. `AKUN-006-DEV-VLESS-WS-59MS` (url=224ms, nekobox=171ms, status=no)
7. `AKUN-004-UNKNOWN-VLESS-WS-55MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS`
10. `AKUN-007-UNKNOWN-VLESS-WS-86MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-82MS`
12. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=197ms, nekobox=171ms, status=no)
13. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
14. `AKUN-010-CLOUDFLARE-VLESS-WS-83MS`
15. `AKUN-016-DE-CLOUDKLEYER-20190515-VLESS-WS-119MS` (url=277ms, status=HTTP 204)
16. `AKUN-017-FASTVPSUS-IPV4-VLESS-WS-95MS` (url=215ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-82MS` (url=229ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-324MS` (url=1472ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-270MS` (url=599ms, status=HTTP 204)
20. `AKUN-023-CLOUDFLARE-VLESS-WS-654MS` (url=1101ms, status=HTTP 204)
21. `AKUN-024-CLOUDFLARE-VLESS-WS-593MS` (url=1039ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-650MS` (url=1297ms, status=HTTP 204)
23. `AKUN-026-UNKNOWN-VLESS-WS-690MS` (url=1116ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-715MS` (url=1193ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-799MS` (url=1091ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
