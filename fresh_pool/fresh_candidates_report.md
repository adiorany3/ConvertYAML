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
1. `AKUN-001-UNKNOWN-VLESS-WS-79MS` (url=225ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-82MS` (url=236ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-86MS` (url=231ms, nekobox=273ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-83MS` (url=231ms, nekobox=245ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-77MS` (url=248ms, nekobox=250ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-98MS` (url=237ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-107MS` (url=265ms, nekobox=260ms, status=yes)
8. `AKUN-008-WPENG-VLESS-WS-92MS` (url=240ms, nekobox=243ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-121MS` (url=208ms, nekobox=252ms, status=yes)
10. `AKUN-010-SAVVY-7-VLESS-WS-96MS` (url=228ms, nekobox=294ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-111MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-95MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=248ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-120MS` (url=249ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-148MS` (url=254ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=232ms, status=HTTP 204)
17. `AKUN-017-UK-GB-DCL-01-20191003-VLESS-WS-137MS` (url=243ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-167MS` (url=256ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-132MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-175MS` (url=234ms, status=HTTP 204)
21. `AKUN-023-RS-RAPIDSEEDBOX-20190717-VLESS-WS-418MS` (url=1352ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-638MS` (url=1084ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-651MS` (url=1057ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-707MS` (url=1276ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-754MS` (url=1215ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
