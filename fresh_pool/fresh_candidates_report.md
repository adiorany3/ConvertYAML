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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=237ms, nekobox=247ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-65MS` (url=230ms, nekobox=256ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-74MS` (url=244ms, nekobox=281ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=257ms, nekobox=248ms, status=yes)
5. `AKUN-005-877774-VLESS-WS-83MS` (url=216ms, nekobox=269ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-66MS` (url=223ms, nekobox=272ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-79MS` (url=236ms, nekobox=276ms, status=yes)
8. `AKUN-008-LEVIKOGJGFDD-VLESS-WS-64MS` (url=234ms, nekobox=266ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-62MS` (url=248ms, nekobox=265ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-68MS` (url=230ms, nekobox=265ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-88MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=307ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-251MS` (url=628ms, status=HTTP 204)
14. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-246MS` (url=527ms, status=HTTP 204)
15. `AKUN-018-UNKNOWN-VLESS-WS-381MS` (url=837ms, status=HTTP 204)
16. `AKUN-019-CLOUDFLARE-VLESS-WS-449MS` (url=780ms, status=HTTP 204)
17. `AKUN-020-SUKARIO-VLESS-WS-426MS` (url=730ms, status=HTTP 204)
18. `AKUN-021-CLOUDFLARE-VLESS-WS-370MS` (url=734ms, status=HTTP 204)
19. `AKUN-022-CLOUDFLARE-VLESS-WS-450MS` (url=982ms, status=HTTP 204)
20. `AKUN-025-UNKNOWN-VLESS-WS-418MS` (url=692ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-525MS` (url=929ms, status=HTTP 204)
22. `AKUN-027-AS199785-DE-IPV4-VLESS-WS-540MS` (url=941ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-551MS` (url=803ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-594MS` (url=954ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-566MS` (url=923ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
