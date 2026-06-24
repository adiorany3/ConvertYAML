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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=225ms, nekobox=240ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-69MS` (url=227ms, nekobox=229ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-104MS` (url=218ms, nekobox=192ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-107MS`
5. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-124MS`
6. `AKUN-006-SPEEDTEST-VLESS-WS-89MS` (url=214ms, nekobox=201ms, status=no)
7. `AKUN-005-UNKNOWN-VLESS-WS-92MS`
8. `AKUN-006-UNKNOWN-VLESS-WS-71MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-154MS` (url=228ms, nekobox=185ms, status=no)
10. `AKUN-007-UNKNOWN-VLESS-WS-141MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-141MS` (url=209ms, nekobox=182ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-92MS` (url=214ms, nekobox=214ms, status=no)
13. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-127MS`
14. `AKUN-014-DEV-VLESS-WS-112MS` (url=202ms, nekobox=198ms, status=no)
15. `AKUN-009-UNKNOWN-VLESS-WS-240MS`
16. `AKUN-010-CLOUDFLARE-VLESS-WS-282MS`
17. `AKUN-017-UNKNOWN-VLESS-WS-289MS` (url=596ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-287MS` (url=668ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-312MS` (url=511ms, status=HTTP 204)
20. `AKUN-021-WPENG-VLESS-WS-301MS` (url=606ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-280MS` (url=598ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-262MS` (url=798ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-431MS` (url=529ms, status=HTTP 204)
24. `AKUN-029-UNKNOWN-VLESS-WS-562MS` (url=1012ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-524MS` (url=747ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
